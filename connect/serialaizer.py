from .models import OrderTable
from rest_framework import serializers

class OrderTabSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTable
        fields = '__all__'