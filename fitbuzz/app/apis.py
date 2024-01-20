from rest_framework import views, response, status
from drf_yasg.utils import swagger_auto_schema
from . import serializers
from . import services
from . import doc_schemas


class FizzBuzzRequest(views.APIView):
    serializer_class = serializers.FizzBuzzRequestSerializer

    @swagger_auto_schema(request_body=serializer_class, responses=doc_schemas.fitbuzz_response_schema)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            result = services.create_fitbuzz_request(data)
            return response.Response({"result": result})
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Stats(views.APIView):
    serializer_class = serializers.FizzBuzzStatsSerializer

    @swagger_auto_schema(responses=doc_schemas.stats_response_schema,)
    def get(self, request):
        stats = services.get_most_used_request()
        serializer = self.serializer_class(instance=stats)
        return response.Response(serializer.data)

