from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from myapp.views import  UserViewSet, ManageUserView,GetUserAvatarNumber

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('myself/', ManageUserView.as_view(), name='myself'),
    path('', include(router.urls)),
    path('get-avatar-number/', GetUserAvatarNumber.as_view()),
]
