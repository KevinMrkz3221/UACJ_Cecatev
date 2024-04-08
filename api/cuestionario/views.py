from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

from rest_framework.viewsets import ModelViewSet

from .serializers import FormTypeSerializer, QuestionSerializer
from .models import FormType, Question
# Create your views here.

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class FormTypeViewSet(ModelViewSet):
    serializer_class = FormTypeSerializer
    queryset = FormType.objects.all()

    http_method_names = ['get', 'post', 'put', 'options']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    http_method_names = ['get', 'post', 'put', 'options'] 


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)