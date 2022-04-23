from rest_framework import serializers
from news.models import News


class NewsUpdateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=True)

    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ['is_from_api', 'time', 'added_at']
        extra_kwargs = {
            "id": {
                "required": True
            },
            "title": {
                "required": True
            },
            "author": {
                "required": True
            },
            "type": {
                "required": True,
            },
            "score": {
                "required": True
            }
        }
