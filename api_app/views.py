# from django.contrib.auth import authenticate
# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
#
# # Create your views here.
#
# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#
#         # Authenticate the user
#         user = authenticate(username=username, password=password)
#         if user is None:
#             return Response({'error': 'Invalid credentials'}, status=401)
#
#         # Generate access and refresh tokens
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'access_token': str(refresh.access_token),
#             'refresh_token': str(refresh)
#         })