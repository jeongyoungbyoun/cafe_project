from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils import timezone

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length = 12, null = True, blank= True) #null 데이터 없음을 증명 blank :
    birth = models.DateField(default=timezone.now, null = True, blank= True)


