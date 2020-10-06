"""Settings for local development."""

from zoho_reports.settings.base import *  # pylint: disable=wildcard-import

DEBUG = True

ENABLE_AUTO_AUTH = True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False

# Set these to the correct values for your OAuth2 Connect provider (e.g., devstack)
SOCIAL_AUTH_EDX_OAUTH2_KEY = "zoho_reports"
SOCIAL_AUTH_EDX_OAUTH2_SECRET = "open_secret"
SOCIAL_AUTH_EDX_OAUTH2_URL_ROOT = "http://localhost:18000"
SOCIAL_AUTH_EDX_OAUTH2_PUBLIC_URL_ROOT = "http://localhost:18000"
# HACK: This is set locally to simulate the scenario when we have an Oauth2 application
#  with the following parameters:
#   - client_id: username
#   - client_secret password
#   - client_type: Public
#   - grant_type: Resource owner password-based
SOCIAL_AUTH_EDX_OAUTH2_AUTHORIZATION_HEADER = 'Basic dXNlcm5hbWU6cGFzc3dvcmQ='
