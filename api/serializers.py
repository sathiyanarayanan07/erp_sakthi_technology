from rest_framework import serializers
from . models import role1,product_details


class role1Serializer(serializers.ModelSerializer):
    class Meta:
        model = role1
        fields = "__all__"

class product_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_details
        fields = "__all__"
