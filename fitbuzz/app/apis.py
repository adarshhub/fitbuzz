from rest_framework import views, response, status
from . import serializers
from . import services


class FizzBuzzRequest(views.APIView):
    def post(self, request):
        serializer = serializers.FizzBuzzRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            result = services.create_fitbuzz_request(data)
            return response.Response({"result": result})
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Stats(views.APIView):
    def get(self, request):
        stats = services.get_most_used_request()
        serializer = serializers.FizzBuzzStatsSerializer(instance=stats)
        return response.Response(serializer.data)

