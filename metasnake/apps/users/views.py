import json
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from metasnake.apps.users.functions import *
from django.core.exceptions import ObjectDoesNotExist
from metasnake.apps.users.docs import *


class LoginView(APIView):
    @swagger_auto_schema(
        operation_summary="Login and Get Tokens",
        operation_description="This endpoint authenticates a user and returns access and refresh tokens.",
        request_body=login_request_body,
        responses=login_responses
    )
    def post(self, request):
        """Login and get tokens"""
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        if not email or not password:
            return HttpResponse(
                json.dumps({'state': 'error', 'message': 'Password or email not provided', 'details': {},
                            'instance': request.path},
                           ensure_ascii=False), status=400)

        user = authenticate(email=email, password=password)
        if user is not None:
            response = HttpResponse()
            tokens = get_tokens_for_user(user.id)
            access_token, access_exp = tokens['access'], tokens['access_exp']
            refresh_token, refresh_exp = tokens['refresh'], tokens['refresh_exp']

            response.set_cookie(
                key='refresh_token',
                value=refresh_token,
                expires=tokens['refresh_exp'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            )
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=access_token,
                expires=tokens['access_exp'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            )

            request.session['email'] = user.email
            request.session['id'] = user.id
            return response
        else:
            return HttpResponse(
                json.dumps({'state': 'error', 'message': 'Invalid email or password', 'details': {},
                            'instance': request.path},
                           ensure_ascii=False), status=401)


class LogoutView(APIView):
    @swagger_auto_schema(
        operation_summary="Logout user",
        operation_description="This endpoint invalidate an user.",
        responses=logout_responses
    )
    def get(self, request):
        response = HttpResponse()
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        del response.headers['Authorization']
        return response


class JWTCheckingView(APIView):
    def get(self, request):
        return HttpResponse('Tokens are valid')


class UserInfoView(APIView):
    @swagger_auto_schema(
        operation_summary="Get User Information",
        operation_description="This endpoint retrieves information about the authenticated user.",
        responses=userinfo_responses
    )
    def get(self, request):
        try:
            user_id = request.user_id
            user = User.objects.get(id=user_id)
            data = {
                'email': user.email,
                'name': user.name,
            }
            return HttpResponse(json.dumps(data, ensure_ascii=False), status=200)
        except ObjectDoesNotExist:
            return HttpResponse(
                json.dumps({'state': 'error', 'message': 'User not found', 'details': {},
                            'instance': request.path},
                           ensure_ascii=False), status=404)


class RegisterView(APIView):
    @swagger_auto_schema(
        operation_summary="Login and Get Tokens",
        operation_description="This endpoint authenticates a user and returns access and refresh tokens.",
        request_body=login_request_body,
        responses=login_responses
    )
    def post(self, request):
        """Login and get tokens"""
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        if not email or not password:
            return HttpResponse(
                json.dumps({'state': 'error', 'message': 'Password or email not provided', 'details': {},
                            'instance': request.path},
                           ensure_ascii=False), status=400)

        user = authenticate(email=email, password=password)
        if user is not None:
            response = HttpResponse()
            tokens = get_tokens_for_user(user.id)
            access_token, access_exp = tokens['access'], tokens['access_exp']
            refresh_token, refresh_exp = tokens['refresh'], tokens['refresh_exp']

            response.set_cookie(
                key='refresh_token',
                value=refresh_token,
                expires=tokens['refresh_exp'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            )
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=access_token,
                expires=tokens['access_exp'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            )

            request.session['email'] = user.email
            request.session['id'] = user.id
            return response
        else:
            return HttpResponse(
                json.dumps({'state': 'error', 'message': 'Invalid email or password', 'details': {},
                            'instance': request.path},
                           ensure_ascii=False), status=401)