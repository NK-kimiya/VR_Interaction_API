from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import uuid
import random

class CustomModel(models.Model):
    name = models.CharField(max_length=255,unique=True)
    _password = models.CharField(max_length=255, db_column='password')
    id = models.BigIntegerField(primary_key=True, editable=False, unique=True)
    avatart_number = models.IntegerField(default=0)
    def set_password(self, raw_password):
        self._password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self._password)

    def save(self, *args, **kwargs):
        if not self.id:  
            self.id = self.generate_unique_id()
        if not self.pk:  # only hash the password if it's a new object
            self._password = make_password(self._password)
        super().save(*args, **kwargs)
    @staticmethod
    def generate_unique_id():
        id = random.randint(1000000000, 9999999999)  # Generate a random 10-digit number
        while CustomModel.objects.filter(id=id).exists():  # Check for collisions
            id = random.randint(1000000000, 9999999999)
        return id
    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ['name', '_password']
