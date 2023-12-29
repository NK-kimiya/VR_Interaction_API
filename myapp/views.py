from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer,AvatarNumberSerializer
from .ownpermissions import ProfilePermission
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
#CRUDに対応したクラス
class UserViewSet(viewsets.ModelViewSet):
    #Userモデルの全インスタンスを対象とするクエリセットを定義
    queryset = CustomUser.objects.all()
    #データのシリアライズ（モデルインスタンスをJSONに変換するプロセス)
    # に使用するシリアライザを指定
    serializer_class = UserSerializer
    #ビューセットにアクセスするための権限クラスを指定
    #特定のアクションを実行するためのユーザー権限
    permission_classes = (ProfilePermission,)

#特定のオブジェクトの取得（Retrieve）と更新（Update）のための汎用ビュー
class ManageUserView(generics.RetrieveUpdateAPIView):
    #データのシリアライズ（モデルインスタンスをJSONに変換するプロセス）に使用する
    # シリアライザを指定します。ここでは、UserSerializerが使用
    serializer_class = UserSerializer
    #ビューにアクセスするユーザーを認証するためのクラスを指定します。
    # この例では、TokenAuthenticationが
    # 使用されており、トークンベースの認証方式を意味
    authentication_classes = (TokenAuthentication,)
    #ビューにアクセスするための権限を制御するクラスを指定します。IsAuthenticated は、
    # ユーザーがログインしている必要がある
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

#TDO:unityからユーザーIDを受け取って、ユーザーをフィルターして、そのuseridだけを
#レスポンスする。パスワードとユーザー名はアクセスできないように設定する。
class GetUserAvatarNumber(APIView):
    def post(self, request, format=None):
        userid = request.data.get('userid')
        user = CustomUser.objects.filter(userid=userid).first()
        if user:
            serializer = AvatarNumberSerializer(user)
            return Response(serializer.data)
        return Response({"message": "User not found"}, status=404)

