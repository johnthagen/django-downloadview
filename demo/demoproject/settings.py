# -*- coding: utf-8 -*-
"""Django settings for Django-DownloadView demo project."""
from os.path import abspath, dirname, join


# Configure some relative directories.
demoproject_dir = dirname(abspath(__file__))
demo_dir = dirname(demoproject_dir)
root_dir = dirname(demo_dir)
data_dir = join(root_dir, 'var')


# Mandatory settings.
ROOT_URLCONF = 'demoproject.urls'
WSGI_APPLICATION = 'demoproject.wsgi.application'


# Database.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(data_dir, 'db.sqlite'),
    }
}


# Required.
SECRET_KEY = "This is a secret made public on project's repository."

# Media and static files.
MEDIA_ROOT = join(data_dir, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = join(data_dir, 'static')
STATIC_URL = '/static/'


# Applications.
INSTALLED_APPS = (
    # Standard Django applications.
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # The actual django-downloadview demo.
    'demoproject',
    'demoproject.object',  # Demo around ObjectDownloadView
    'demoproject.storage',  # Demo around StorageDownloadView
    'demoproject.path',  # Demo around PathDownloadView
    'demoproject.http',  # Demo around HTTPDownloadView
    'demoproject.virtual',  # Demo around VirtualDownloadView
    'demoproject.nginx',  # Sample optimizations for Nginx X-Accel.
    # For test purposes. The demo project is part of django-downloadview
    # test suite.
    'django_nose',
)


# Middlewares.
MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django_downloadview.DownloadDispatcherMiddleware'
]


# Uncomment the following lines to enable global Nginx optimizations.
DOWNLOADVIEW_MIDDLEWARES = (
    ('default', 'django_downloadview.nginx.XAccelRedirectMiddleware',
                {'source_url': '/media/nginx/',
                 'destination_url': '/nginx-optimized-by-middleware/'}),
)


# Development configuration.
DEBUG = True
TEMPLATE_DEBUG = DEBUG
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--verbose',
             '--nocapture',
             '--rednose',
             '--with-id',  # allows --failed which only reruns failed tests
             '--id-file=%s' % join(data_dir, 'test', 'noseids'),
             '--with-doctest',
             '--with-xunit',
             '--xunit-file=%s' % join(data_dir, 'test', 'nosetests.xml'),
             '--with-coverage',
             '--cover-erase',
             '--cover-package=django_downloadview',
             '--no-path-adjustment',
             '--all-modules',
             ]
