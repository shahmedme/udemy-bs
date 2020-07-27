import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'somesecretkey'

DEBUG = False

ALLOWED_HOSTS = ['*']

DB_CONFIG = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}

DEFAULT_FILE_STORAGE = 'wd.storage.AzureMediaStorage'
STATICFILES_STORAGE = 'wd.storage.AzureStaticStorage'

STATIC_LOCATION = "static"
MEDIA_LOCATION = "media"

AZURE_ACCOUNT_NAME = "azureaccountname"
AZURE_ACCOUNT_KEY = 'azureaccountkey'
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'