"""Settings for local development."""

import os

import dj_database_url

from zoho_reports.settings.base import *  # pylint: disable=wildcard-import

ALLOWED_HOSTS = ["*"]

SOCIAL_AUTH_EDX_OAUTH2_KEY = os.environ.get("EDX_OAUTH2_KEY", "")
SOCIAL_AUTH_EDX_OAUTH2_SECRET = os.environ.get("EDX_OAUTH2_SECRET", "")
SOCIAL_AUTH_EDX_OAUTH2_URL_ROOT = os.environ.get("EDX_OAUTH2_URL_ROOT", "")
SOCIAL_AUTH_EDX_OAUTH2_PUBLIC_URL_ROOT = os.environ.get("EDX_OAUTH2_PUBLIC_URL_ROOT", "")
SOCIAL_AUTH_EDX_OAUTH2_AUTHORIZATION_HEADER = os.environ.get("EDX_OAUTH2_AUTHORIZATION_HEADER", "")

# Update database settings from the environment variable DATABASE_URL.
DATABASES['default'].update(dj_database_url.config())

# Simplified static file serving.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
WHITENOISE_MANIFEST_STRICT = False
