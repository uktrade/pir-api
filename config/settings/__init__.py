"""
Django settings for invest project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import dj_database_url
import os

from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG') == 'true'
ENABLE_DEBUG_TOOLBAR = os.getenv('ENABLE_DEBUG_TOOLBAR') == 'true'

if ENABLE_DEBUG_TOOLBAR:
    INTERNAL_IPS = os.getenv('INTERNAL_IPS', ['127.0.0.1'])

# As the app is running behind a host-based router supplied by Heroku or other
# PaaS, we can open ALLOWED_HOSTS
# For Cloudflare, disallow access to the CF url, by seting ALLOWED_HOSTS
# to the external url, e.g: ALLOWED_HOSTS=invest.great.uat.uktrade.io
ALLOWED_HOSTS = [
  '*'
]

RESTRICT_ADMIN = True  # block the django admin at /django-admin
RESTRICT_URLS = ['^admin/*']  # block the wagtail admin
ALLOWED_ADMIN_IPS = [item.strip()
                     for item in
                     os.getenv('ALLOWED_ADMIN_IPS', '127.0.0.1').split(',')
                     ]

REDIS_URL = os.getenv("REDIS_URL")
ENABLE_REDIS = REDIS_URL is not None

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'storages',
    'modeltranslation',
    'moderation',

    'investment_report',

    'crispy_forms',
    'modelcluster',
    'taggit',
    'captcha',
    'clear_cache',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'markdownx',
    'sorl.thumbnail',
    'django_countries',
    'countries_plus',
    'bootstrap4',
    'rest_framework',
]

try:
    import django_extensions  # noqa: F401
except ImportError:
    pass
else:
    INSTALLED_APPS.append('django_extensions')


if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',   # position - after: SessionMiddleWare, before: CommonMiddleWare  # noqa
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

if ENABLE_DEBUG_TOOLBAR:
    MIDDLEWARE.append(
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    )

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# AWS for Django storages
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_DEFAULT_REGION=os.environ.get('AWS_DEFAULT_REGION', 'eu-west-1')

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}

if ENABLE_REDIS:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": REDIS_URL,
            'TIMEOUT': 60,
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', _(u'English')),
    ('de', _(u'German')),
    ('es', _(u'Spanish')),
    ('fr', _(u'French')),
    ('pt', _(u'Portugese')),
    ('ar', _(u'Arabic')),
    ('ja', _(u'Japanese')),
    ('zh-cn', _(u'Simplified Chinese')),
)

MODELTRANSLATION_FALLBACK_LANGUAGES = tuple()

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# needed only for dev local storage
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
if AWS_ACCESS_KEY_ID is None:
    MEDIA_URL = '/media/'
else:
    MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN
    DEFAULT_FILE_STORAGE = 'config.s3.MediaRootS3BotoStorage'
    STATICFILES_STORAGE = 'config.s3.StaticRootS3BotoStorage'

# Static files served with Whitenoise and AWS Cloudfront
# http://whitenoise.evans.io/en/stable/django.html#instructions-for-amazon-cloudfront
# http://whitenoise.evans.io/en/stable/django.html#restricting-cloudfront-to-static-files
STATIC_URL = "https://%s/static/" % AWS_S3_CUSTOM_DOMAIN

# Logging for development
if DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['console'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }
else:
    # Sentry logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s '
                          '%(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',
                'class': (
                    'raven.contrib.django.raven_compat.handlers.SentryHandler'
                ),
                'tags': {'custom-tag': 'x'},
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
        },
    }

SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT', 'true') == 'true'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
SECURE_HSTS_SECONDS = int(os.getenv('SECURE_HSTS_SECONDS', '16070400'))
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Sentry
RAVEN_CONFIG = {
    "dsn": os.getenv("SENTRY_DSN"),
    "processors": (
        'raven.processors.SanitizePasswordsProcessor',
        'config.sentry_processors.SanitizeEmailMessagesProcessor',
    )
}

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'true') == 'true'

CLOUDFRONT_DISTRIBUTION_ID = os.getenv('CLOUDFRONT_DISTRIBUTION_ID')
if CLOUDFRONT_DISTRIBUTION_ID:
    WAGTAILFRONTENDCACHE = {
        'cloudfront': {
            'BACKEND': 'wagtail.contrib.frontend_cache.backends.CloudfrontBackend',  # noqa
            'DISTRIBUTION_ID': CLOUDFRONT_DISTRIBUTION_ID,
        },
    }

MARKDOWNX_MARKDOWN_EXTENSIONS = ['markdown.extensions.footnotes']
MARKDOWNX_UPLOAD_CONTENT_TYPES = ['image/png', 'image/jpeg', 'image/svg+xml']
SITE_ID = 1

EMAIL_BACKEND = 'django_amazon_ses.EmailBackend'
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_FROM', 'rollokb@gmail.com')


MODERATION_MODERATORS = [item.strip()
    for item in
    os.getenv('MODERATION_MODERATORS', 'rollokb@gmail.com').split(',')
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'config.permissions.SignatureCheckPermission',
    )
}


SIGNATURE_SECRET = os.getenv('SIGNATURE_SECRET', 'abc')

CELERY_BROKER_URL = REDIS_URL