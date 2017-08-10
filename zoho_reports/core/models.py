""" Core models. """

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """Custom user model for use with OpenID Connect."""
    full_name = models.CharField(_('Full Name'), max_length=255, blank=True, null=True)

    @property
    def access_token(self):
        """ Returns an OAuth2 access token for this user, if one exists; otherwise None.

        Assumes user has authenticated at least once with edX Open ID Connect.
        """
        try:
            return self.social_auth.first().extra_data[u'access_token']  # pylint: disable=no-member
        except Exception:  # pylint: disable=broad-except
            return None

    class Meta(object):  # pylint:disable=missing-docstring
        get_latest_by = 'date_joined'

    def get_full_name(self):
        return self.full_name or super(User, self).get_full_name()

    def __str__(self):
        return str(self.get_full_name())


class Page(models.Model):
    """A static HTML page."""

    path = models.SlugField(
        "URL path",
        max_length=255,
        help_text="The URL path the page will be available at.",
    )
    html = models.TextField(
        "Page source",
        help_text="The HTML source code of the page.",
    )
    _allowed_emails = models.CharField(
        "Allowed users",
        max_length=511,
        blank=True,
        db_column="allowed_users",
        help_text="Comma-seprateed list of email addresses with access to the page",
    )

    @property
    def allowed_emails(self):
        "The allowed email addresses as a list"
        return [email.strip().lower() for email in self._allowed_emails.split(",")]

    def has_access(self, user):
        """Return a bool indicating whether the given Django user has access to the page."""
        return user is not None and (
            user.is_staff or
            user.email.lower() in self.allowed_emails
        )

    def __str__(self):
        return "Page at /{}/".format(self.path)
