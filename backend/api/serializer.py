from rest_framework import serializers
from .models import Tower


class TowerSerializer(serializers.ModelSerializer):

    mcc = serializers.CharField(required=False)
    net = serializers.CharField(required=False)
    area = serializers.CharField(required=False)
    cell = serializers.CharField(required=False)

    class Meta:
        model = Tower
        fields = ('mcc', 'net', 'area', 'cell')


