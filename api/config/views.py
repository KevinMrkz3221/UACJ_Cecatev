from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .serializers import UserSerializer

from django.contrib.auth.models import User



@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username']) 
        user.set_password(serializer.data['password'])
        user.save()

        return Response({
            "status": status.HTTP_201_CREATED
        })
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
