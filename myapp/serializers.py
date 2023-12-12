from rest_framework import serializers
from .models import CustomModel

class CustomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomModel
        fields = '__all__'
