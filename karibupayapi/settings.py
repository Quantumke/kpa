"""
Django settings for karibupayapi project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@s+8ufkiu4*0-k2+hoa3k9ov@%^t*c*u0eaqg(*5b5fnh@g)(@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'mpesa',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'karibupayapi.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.realpath(os.path.dirname(__file__)), '../templates'),
)



WSGI_APPLICATION = 'karibupayapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'karibupay_api',
        'USER': 'root',
        'PASSWORD': 'master12!',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'social.backends.github.GithubOAuth2',
   'django.contrib.auth.backends.ModelBackend',

)
LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_FACEBOOK_KEY = '1060370770699874'
SOCIAL_AUTH_FACEBOOK_SECRET ='4835f0058cda5fafeabba85ae61ff5c4'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '624247672272-ee5po8ap7p56kkb9bupdoa1gibkf0in7.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'sdsA2HP-nXt3ycUUOlHsj6a9'

SOCIAL_AUTH_GITHUB_KEY = 'af06ca932a7a0032bc93'
SOCIAL_AUTH_GITHUB_SECRET = 'e0f34643f41fabef824e6e1bcdc376fe35daef9f'

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '77rjwgm5u2jiuk'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = '88bhqkaBJjKsPSP8'

SOCIAL_AUTH_TWITTER_KEY = '01am3mjPMK1zWsXOv8Fmtagw8'
SOCIAL_AUTH_TWITTER_SECRET = 'HLFUM2FoYxcJv83ADOF6jkY6LFVoXLbviA15G3nq0gy484Qfsf'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
