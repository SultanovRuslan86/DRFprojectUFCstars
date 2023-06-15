from rest_framework import serializers
from .models import Ufsstars

class UfsstarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ufsstars
        fields = ('name', 'weight')

