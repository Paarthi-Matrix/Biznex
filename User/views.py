import json

from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.views import View

from validator.input_validators import validate_user_inputs
from .models import User
from util.data_conversion_util import to_user


class Registration(View):
    def post(self, request,  *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))

            error_message = validate_user_inputs(data)
            if error_message is not None:
                return HttpResponse(error_message, status=400)

            user = to_user(data)
            user.save()

            return HttpResponse({
                "message": "User created successfully",
                "user_id": str(user.user_id),
                "name": user.name
            }, status=201)

        except json.JSONDecodeError:
            print("invalid json")
            return HttpResponse({"error": "Invalid JSON format"}, status=400)

        except ValidationError as e:
            return HttpResponse({"error": str(e)}, status=400)
