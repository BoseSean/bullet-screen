from rest_framework import serializers
from .models import Bul

class BulSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bul