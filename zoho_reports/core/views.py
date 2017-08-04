"""Core views."""
import logging
import uuid

from django.conf import settings
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View

from zoho_reports.core.models import Page


logger = logging.getLogger(__name__)
User = get_user_model()


class AutoAuth(View):
    """Creates and authenticates a new User with superuser permissions.

    If the ENABLE_AUTO_AUTH setting is not True, returns a 404.
    """

    def get(self, request):
        """
        Create a new User.

        Raises Http404 if auto auth is not enabled.
        """
        if not getattr(settings, 'ENABLE_AUTO_AUTH', None):
            raise Http404

        username_prefix = getattr(settings, 'AUTO_AUTH_USERNAME_PREFIX', 'auto_auth_')

        # Create a new user with staff permissions
        username = password = username_prefix + uuid.uuid4().hex[0:20]
        User.objects.create_superuser(username, email=None, password=password)

        # Log in the new user
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect(settings.LOGIN_REDIRECT_URL)


class IndexView(LoginRequiredMixin, View):
    """Require login and redirect users to a useful page."""

    def get(self, request):
        """Require login and redirect users to a useful page."""
        if request.user.is_superuser:
            return redirect(reverse("admin:index"))
        for page in Page.objects.iterator():
            if page.has_access(request.user):
                return redirect(reverse("static_page", kwargs=dict(path=page.path)))
        return HttpResponse("You do not have access to any page on this site.")


class PageView(LoginRequiredMixin, View):
    """Check user access and render static page."""

    def get(self, request, path):
        """Check user access and render static page."""
        page = get_object_or_404(Page, path=path)
        if not page.has_access(request.user):
            raise Http404
        return HttpResponse(page.html)
