from rest_framework import serializers
from . models import role1


class role1Serializer(serializers.ModelSerializer):
    class Meta:
        model = role1
        fields = "__all__"

