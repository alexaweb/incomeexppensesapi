"""
Django settings for incomeexpensesapi project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import datetime
import dj_database_url
import environ


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Initialise environment variables
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# False if not in os.environ because of casting above
DEBUG = True
#env('DEBUG')

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(' ')


AUTH_USER_MODEL = 'authentication.User'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'drf_yasg',
    'authentication',
    'expenses',
    'income',
    'anymail'
]

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'incomeexpensesapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'incomeexpensesapi.wsgi.application'

# CORS WHITELIST
CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "https://relaxed-curie-e9a516.netlify.app",
    "http://127.0.0.1:8080"
]

CORS_ORIGIN_REGEX_WHITELIST = [
    r"^https://\w+\.netlify\.app$",
]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': env('cobsdevelopment', # database name
#        'USER': 'cobs',
#        'PASSWORD': 'cobs.pwd',
#        'HOST': 'localhost',
#        'PORT': '3306',
#    }
#}

if env('DATABASE_URL'):
    DATABASES = {'default': dj_database_url.config(default=env('DATABASE_URL'))}

#mysql://USER:PASSWORD@HOST:PORT/NAME
#DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=1),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.mailgun.org'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = env('EMAIL_HOST_USER')
#EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')


ANYMAIL_MAILGUN_API_KEY = env('MAILGUN_API_KEY')
ANYMAIL_MAILGUN_SENDER_DOMAIN = env('MAILGUN_DOMAIN')
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
DEFAULT_FROM_EMAIL = env('EMAIL_FROM')  # if you don't already have this in settings
SERVER_EMAIL = env('EMAIL_FROM')  # ditto (default from-email for Django errors)
