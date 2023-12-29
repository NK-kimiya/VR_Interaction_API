from django.db import models
from django.contrib.auth.models import AbstractUser
import random

class CustomUser(AbstractUser):
    avatart_number = models.IntegerField(default=0)
    userid = models.BigIntegerField(unique=True, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.userid:
            self.userid = self.generate_unique_id()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_id():
        userid = random.randint(1000000000, 9999999999)
        while CustomUser.objects.filter(userid=userid).exists():
            userid = random.randint(1000000000, 9999999999)
        return userid

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'