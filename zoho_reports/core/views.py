"""Core views."""
import logging
import uuid

from django.conf import settings
from django.contrib.auth import get_user_model, login, authenticate
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import View


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
