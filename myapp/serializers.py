from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        #シリアライズに含めるフィールドを指定
        fields = ['id', 'username', 'password', 'avatart_number','userid']
        #password フィールドが書き込み専用であり、必須であることを指定
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    #クライアントから受け取ったデータ）を使って
    # 新しい User オブジェクトを作成
    def create(self, validated_data):
        #バリデーションされたデータをもとにユーザーを作成します。
        user = CustomUser.objects.create_user(**validated_data)
        #新しいユーザーに対して認証トークンを生成
        Token.objects.create(user=user)
        return user


class AvatarNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['avatart_number']