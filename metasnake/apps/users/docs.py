from drf_yasg import openapi

login_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "email": openapi.Schema(type=openapi.TYPE_STRING, description="Email of the user.", example="test@test.ru"),
        "password": openapi.Schema(type=openapi.TYPE_STRING, description="Password of the user.", example="12345678")
    },
    required=["email", "password"],
)

userinfo_responses = {
    200: openapi.Schema(type=openapi.TYPE_OBJECT,
                        properties={
                            "email": openapi.Schema(
                                type=openapi.TYPE_STRING,
                                description="email of the user.",
                                example="test@test.ru"
                            )
                        })
}

login_responses = {
    200: openapi.Schema(type=openapi.TYPE_OBJECT, properties={}),
}

logout_responses = {
    200: openapi.Schema(type=openapi.TYPE_OBJECT, properties={}),
}
