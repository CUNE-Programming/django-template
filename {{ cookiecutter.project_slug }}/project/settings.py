"""
Django settings for project.

Generated by CPT-Django-Template using Cookiecutter template.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings
"""
import os
from pathlib import Path
import environ

env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django_vite',
    {% if cookiecutter.stack == 'THAD' %}'django_htmx',
    'template_partials',{% endif %}
    {% if cookiecutter.stack == 'DIRT'%}'inertia',{%endif %}
    'apps.cpt',
]

if DEBUG:
    INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE = []
if DEBUG:
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    {% if cookiecutter.stack == 'THAD' %}"django_htmx.middleware.HtmxMiddleware"{% endif %}
    {% if cookiecutter.stack == 'DIRT' %}"inertia.middleware.InertiaMiddleware"{% endif %}
]

{% if cookiecutter.stack == 'DIRT' %}INERTIA_LAYOUT = 'application.html'{% endif %}

INTERNAL_IPS = [
    "127.0.0.1"
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages"
            ],
            "builtins": [
                "django_vite.templatetags.django_vite",
                "django.contrib.staticfiles.templatetags.static",
                {% if cookiecutter.stack == 'THAD' %}"template_partials.templatetags.partials"{% endif %},
            ]
        }
    }
]

WSGI_APPLICATION = "project.wsgi.application"

DATABASES = {"default": env.db()}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.validation.CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.validation.NumericPasswordValidator"
    }
]

DJANGO_VITE = {
    "default": {
        "dev": DEBUG
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Chicago"

USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIR = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"