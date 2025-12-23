"""
Django settings for config project.
"""

import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv  # Cần cài đặt: pip install python-dotenv

# Tải biến môi trường từ file .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# 1. BẢO MẬT & MÔI TRƯỜNG (SECURITY)
# ==============================================================================
# Lấy Secret Key từ biến môi trường, không hardcode trong code
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-fallback-key-for-dev-only')

# Chạy Debug hay không tùy thuộc vào môi trường
DEBUG = os.getenv('DEBUG') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')


# ==============================================================================
# 2. ỨNG DỤNG (APPLICATIONS)
# ==============================================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # --- Third Party Apps ---
    'rest_framework',
    'rest_framework_simplejwt',  # Xác thực JWT
    'corsheaders',               # Cho phép Frontend gọi API

    # --- Local Apps (Modules nghiệp vụ) ---
    'apps.users',
    'apps.products',
    'apps.routines',
    'apps.orders',
    # 'apps.common', # Bật lên nếu trong common có models hoặc template tags
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # [QUAN TRỌNG] Phải đặt trên cùng
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# ==============================================================================
# 3. CƠ SỞ DỮ LIỆU (DATABASE)
# ==============================================================================
# Mặc định dùng SQLite cho Dev. Production nên đổi sang PostgreSQL.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / os.getenv('DB_NAME', 'db.sqlite3'),
    }
}


# ==============================================================================
# 4. USER CUSTOM & AUTHENTICATION
# ==============================================================================
# Chỉ định model User tùy chỉnh nằm trong app users
AUTH_USER_MODEL = 'users.User'

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


# ==============================================================================
# 5. CẤU HÌNH API (REST FRAMEWORK & JWT)
# ==============================================================================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # Mặc định chặn tất cả, phải mở công khai thủ công
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer', 
        # Nếu bạn đã tạo file custom renderer thì bỏ comment dòng dưới và xóa dòng trên
        # 'apps.utils.renderers.CustomJSONRenderer', 
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# Cấu hình CORS (Cho phép mọi nguồn truy cập trong lúc Dev)
CORS_ALLOW_ALL_ORIGINS = True 


# ==============================================================================
# 6. QUỐC TẾ HÓA (INTERNATIONALIZATION)
# ==============================================================================
LANGUAGE_CODE = 'vi'  # Tiếng Việt

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_TZ = True


# ==============================================================================
# 7. STATIC FILES
# ==============================================================================
STATIC_URL = 'static/'

# Nơi gom static file khi chạy lệnh collectstatic (Dùng cho Production)
STATIC_ROOT = BASE_DIR / 'staticfiles'