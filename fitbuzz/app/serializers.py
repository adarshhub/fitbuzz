from rest_framework import serializers
from .models import FizzBuzzRequest, Stats

class FizzBuzzRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FizzBuzzRequest
        fields = '__all__'


class FizzBuzzStatsSerializer(serializers.ModelSerializer):
    request_params = serializers.SerializerMethodField()

    def get_request_params(self, obj):
        return obj.request.get_params_dict()

    class Meta:
        model = Stats
        fields = ('request_params', 'hits')