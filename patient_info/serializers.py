from rest_framework import serializers
from .models import PDocs


class PDocsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PDocs
        fields = ('id', 'docs', 'owner_id')
