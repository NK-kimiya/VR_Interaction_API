from django.http import HttpResponse
from rest_framework import generics
from .models import CustomModel
from .serializers import CustomModelSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return HttpResponse("Hello, Django!")
class CustomModelListCreateView(generics.ListCreateAPIView):
    queryset = CustomModel.objects.all()
    serializer_class = CustomModelSerializer

@api_view(['POST'])
def get_name_and_id_by_password(request):
    _password = request.data.get('_password')
    _name = request.data.get('name')
    if not _password:
        return Response({"detail": "Password not provided."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        custom_model_instance = CustomModel.objects.get(_password=_password, name=_name)
        serializer = CustomModelSerializer(custom_model_instance)
        return Response({"name": serializer.data['name'], "id": serializer.data['id'],"avatar_number": serializer.data['avatart_number']}, status=status.HTTP_200_OK)
    except CustomModel.DoesNotExist:
        return Response({"detail": "No entry found for the given password."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def get_entry_by_id(request):
    _id = request.data.get('id')
    if not _id:
        return Response({"detail": "ID not provided."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        _id = int(_id)
    except ValueError:
        return JsonResponse({"error": "Invalid ID format. Expected an integer value."}, status=400)
    try:
        custom_model_instance = CustomModel.objects.get(id=_id)
        serializer = CustomModelSerializer(custom_model_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except CustomModel.DoesNotExist:
        return Response({"detail": "No entry found for the given ID."}, status=status.HTTP_404_NOT_FOUND)
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "app/index.html")