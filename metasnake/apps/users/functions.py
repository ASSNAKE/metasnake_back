from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.tokens import RefreshToken
from metasnake.apps.users.models import User
from datetime import datetime


def get_tokens_for_user(user_id):
    try:
        user = User.objects.get(id=user_id)
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        refresh_exp = datetime.utcfromtimestamp(refresh['exp'])
        access_exp = datetime.utcfromtimestamp(access['exp'])
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'refresh_exp': refresh_exp,
            'access_exp': access_exp,
        }
    except ObjectDoesNotExist:
        return {
            'refresh': None,
            'access': None,
            'refresh_exp': None,
            'access_exp': None,
        }
