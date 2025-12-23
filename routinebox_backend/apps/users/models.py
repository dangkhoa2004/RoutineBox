from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Thêm các trường tùy chỉnh nếu cần
    email = models.EmailField(unique=True)
    
    # Định nghĩa role theo SRS [cite: 65]
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Quản trị viên'
        CUSTOMER = 'CUSTOMER', 'Khách hàng'
        
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CUSTOMER)
    
    USERNAME_FIELD = 'email'  # Đăng nhập bằng Email
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email