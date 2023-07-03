from rest_framework import serializers
from .models import Ufsstars

class UfsstarsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Ufsstars
        fields = '__all__'


# class UfsstarsSerializer(serializers.Serializer):
    # name = serializers.CharField(max_length=30)
    # description = serializers.CharField()
    # time_create = serializers.DateTimeField(read_only=True)
    # time_update = serializers.DateTimeField(read_only=True)
    # is_published = serializers.BooleanField(default=True)
    # art_id = serializers.IntegerField()
    # weight_id = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Ufsstars.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.time_create = validated_data.get('time_create', instance.time_create)
    #     instance.time_update = validated_data.get('time_update', instance.time_update)
    #     instance.art_id = validated_data.get('art_id', instance.art_id)
    #     instance.weight_id = validated_data.get('weight_id', instance.weight_id)
    #     instance.save()
    #     return instance



