from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser
from .serializer import RegistrationSerializer, LoginSerializer, UsersListSerializer
from rest_framework import status, permissions

# Create your views here.
class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'User registered successfully',
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.context["user"]
            # Generate access and refresh tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UsersListSerializer(users, many=True)
        return Response({
            "result":serializer.data
        })