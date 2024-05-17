from django.urls import path
from metasnake.apps.users.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [
    #path('get', views.get_users, name='get users'),
    path('auth/login', LoginView.as_view(), name='login'),
    path('auth/logout', LogoutView.as_view(), name='logout'),
    path('auth/check', UserInfoView.as_view(), name='check_auth'),
] + router.urls
