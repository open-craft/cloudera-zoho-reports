"""Settings for local development."""

from zoho_reports.settings.base import *  # pylint: disable=wildcard-import

DEBUG = True

ENABLE_AUTO_AUTH = True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False

# Set these to the correct values for your OAuth2/OpenID Connect provider (e.g., devstack)
SOCIAL_AUTH_EDX_OIDC_KEY = "zoho_reports"
SOCIAL_AUTH_EDX_OIDC_SECRET = "open_secret"
SOCIAL_AUTH_EDX_OIDC_URL_ROOT = "http://localhost:8000/oauth2"
SOCIAL_AUTH_EDX_OIDC_ISSUER = "http://127.0.0.1:8000/oauth2"
SOCIAL_AUTH_EDX_OIDC_LOGOUT_URL = "http://localhost:8000/logout"
SOCIAL_AUTH_EDX_OIDC_ID_TOKEN_DECRYPTION_KEY = SOCIAL_AUTH_EDX_OIDC_SECRET
