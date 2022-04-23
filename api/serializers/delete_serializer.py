from rest_framework import serializers
from news.models import News


class DeleteSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=True)

    class Meta:
        model = News
        fields = ['id']
