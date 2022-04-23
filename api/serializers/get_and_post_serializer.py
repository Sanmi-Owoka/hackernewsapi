from rest_framework import serializers
from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ['id', 'is_from_api', 'time', 'added_at']
        extra_kwargs = {
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


class GetNews(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
