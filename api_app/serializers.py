from rest_framework import serializers
from .models import A

class ASerializer(serializers.ModelSerializer):
    class Meta:
        model = A
        fields = '__all__'
