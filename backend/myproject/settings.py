"""

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import secrets
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.token_urlsafe(50)   

# SECURITY WARNING: don't run with debug turned on in production!
CUURENT_ENV = os.getenv("CURRENT_ENV", "PROD")
if CUURENT_ENV == "DEV":
    DEBUG = True
else:
    DEBUG = False
print("## DEBUG:",DEBUG, flush=True)
print("## CUURENT_ENV:",CUURENT_ENV, flush=True)

ALLOWED_HOSTS = ['13.50.150.80', 'mediumai.space', 'www.mediumai.space', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "myapp.apps.MyappConfig",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'myapp/static')] # old
STATIC_ROOT = BASE_DIR / 'all_static_files' ## bildiğin local bucket, burada toplanan bütün static fileların(default ve bizim belirlediğimiz STATICFILES_DIRS içerisindeki dir'ler) hangi dir'e aktarılcağını belirledik.
STATICFILES_DIRS = [ #DEFAULT STATIC FILELARIN DIŞINDA TOPLAMAK İSTEDİĞİN DIRECTORYLERI BURADAN AYARLIYORSUN (diretoylerin adının static vs olması şart değil)
    BASE_DIR / 'myapp' / 'static', ## Burada kendimiz oluşturduğumuz static dosyalarımızın olduğu dir'i tanımladık
    # BASE_DIR / 'istediğin/path',
]  ## burada static klasörüne nasıl ulaşacağını,pathini tanımladık

MEDIA_URL = '/media/'  # media dosyalarının urlsi, Bunu media pathine giden bir kestirme olarak düşün
MEDIA_ROOT = BASE_DIR / 'all_media_files' ## bildiğin local bucket, burada kullanıcıların vs yüklediği medya dosyalarının hangi dir'e aktarılcağını,yükleneceğini ayarladık.

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


print("## BASE_DIR:",BASE_DIR, flush=True)