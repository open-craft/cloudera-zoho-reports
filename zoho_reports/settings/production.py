"""Settings for local development."""

import os

import dj_database_url

from zoho_reports.settings.base import *  # pylint: disable=wildcard-import

ALLOWED_HOSTS = ["*"]

SOCIAL_AUTH_EDX_OIDC_KEY = os.environ.get("EDX_OIDC_KEY", "")
SOCIAL_AUTH_EDX_OIDC_SECRET = os.environ.get("EDX_OIDC_SECRET", "")
SOCIAL_AUTH_EDX_OIDC_URL_ROOT = os.environ.get("EDX_OIDC_URL_ROOT", "")
SOCIAL_AUTH_EDX_OIDC_ISSUER = os.environ.get("EDX_OIDC_ISSUER", "")
SOCIAL_AUTH_EDX_OIDC_LOGOUT_URL = os.environ.get("EDX_OIDC_LOGOUT_URL", "")
SOCIAL_AUTH_EDX_OIDC_ID_TOKEN_DECRYPTION_KEY = SOCIAL_AUTH_EDX_OIDC_SECRET

# Update database settings from the environment variable DATABASE_URL.
DATABASES['default'].update(dj_database_url.config())

# Simplified static file serving.
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
