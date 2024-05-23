import json
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from metasnake.apps.users.models import User
from django.core.exceptions import ObjectDoesNotExist
from metasnake.apps.data.functions import *
from metasnake.apps.data.docs import *


class Upload(APIView):
    #@swagger_auto_schema(
    #    operation_summary="Upload Information",
    #    operation_description="This endpoint receives data (archive) and saves it to the server.",
    #    manual_parameters=[file_param],
    #    responses=upload_responses
    #)
    def post(self, request):
        try:
            return HttpResponse(json.dumps({}, ensure_ascii=False), status=200)
        except Exception as e:
            return HttpResponse(json.dumps({
                'state': 'error',
                'message': 'Something went wrong',
                'details': {'message': str(e)},
                'instance': request.path,
            }, ensure_ascii=False), status=404)