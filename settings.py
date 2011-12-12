# fBSD-Community-Portal
# Copyright (c) 2011 Nolan Lum <nol888@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

# Django settings for fBSD_Portal project.
from os.path import abspath, dirname, basename, join

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Don't touch these.
ROOT_PATH = abspath(dirname(__file__))
PROJECT_NAME = basename(ROOT_PATH)
# End don't touch these.

ADMINS = (
    ('N Lum', 'nol888@gmail.com')
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(ROOT_PATH, 'sqlite.db'),
        'USER': '', 'PASSWORD': '', 'HOST': '', 'PORT': ''
    }
}

FACEBOOK_APP_ID              = '199624726787942'
FACEBOOK_API_SECRET          = '22ba69397ea5b462b963cbab4d41a9f0'
FACEBOOK_EXTENDED_PERMISSIONS= ['email']
GOOGLE_OAUTH2_CLIENT_ID      = '658227067660.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = '0VlDIC_GaOi8B-n_WFmTR6E-'
GOOGLE_OAUTH_EXTRA_SCOPE     = ['https://www.googleapis.com/auth/userinfo.profile']
LINKEDIN_CONSUMER_KEY        = '4n1683p54hc3'
LINKEDIN_CONSUMER_SECRET     = 'gBv1cJM2CqYiw2LY'
LINKEDIN_EXTRA_FIELD_SELECTORS=['']

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'

SECRET_KEY = 't53xqy+s_p6_ynce#y$hr75_1_)g+%f^v6aczhf%20a8lm8_ps'

SITE_ID = 1

#######################
# DON'T MODIFY BELOW
#######################
USE_I18N = True
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

STATIC_ROOT = join(ROOT_PATH, 'web_static/')
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'fBSD_Portal.portal.middleware.PrivMsgMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'fBSD_Portal.portal.context_processors.privmsgcount',
)

ROOT_URLCONF = 'fBSD_Portal.urls'

TEMPLATE_DIRS = (
    join(ROOT_PATH, 'web_template')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_auth',
    'fBSD_Portal.portal'
)

AUTH_PROFILE_MODULE = 'portal.CommPortalProfile'

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.flickr.FlickrBackend',
    'social_auth.backends.OpenIDBackend',
    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL           = '/'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
