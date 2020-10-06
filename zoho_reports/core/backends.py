"""Custom edX OAuth2 backend."""

from auth_backends.backends import EdXOAuth2
from django.conf import settings


# pylint: disable=abstract-method
class CustomHeaderEdXOAuth2(EdXOAuth2):
    """This subclass allows adding the `Authorization` header to the access token request."""

    def auth_headers(self):
        """
        Allows adding the `Authorization` header by specifying
        `SOCIAL_AUTH_EDX_OAUTH2_AUTHORIZATION_HEADER` in settings.
        """
        headers = super().auth_headers()
        print(headers)
        if (auth_header := settings.SOCIAL_AUTH_EDX_OAUTH2_AUTHORIZATION_HEADER) is not None:
            headers['Authorization'] = auth_header

        return headers
