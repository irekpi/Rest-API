from rest_framework import serializers
from .models import Users


class UsersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    employee_id = serializers.CharField(required=False)
    ranking = serializers.FloatField(required=False)

    class Meta:
        model = Users
        fields = '__all__'