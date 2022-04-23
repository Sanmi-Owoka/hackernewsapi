from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from ..serializers.update_news_serializer import NewsUpdateSerializer
from news.models import News
from django.core.exceptions import ObjectDoesNotExist


class UpdateNewsView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = NewsUpdateSerializer

    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "message": "Failure",
                    "errors": serializer.errors,
                    "data": "null"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        id = serializer.validated_data["id"]
        try:
            news = News.objects.get(is_from_api=False, id=id)
        except ObjectDoesNotExist:
            return Response(
                {
                    'message': 'Cannot modify news item from Hacker News API'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        news.title = serializer.validated_data["title"]
        news.author = serializer.validated_data["author"]
        news.type = serializer.validated_data["type"]
        news.score = serializer.validated_data["score"]
        news.text = serializer.validated_data["text"]
        news.url = serializer.validated_data["score"]
        news.save()
        output = self.serializer_class(news)
        return Response(
            {
                "message": "Success",
                "data": output.data,
                "errors": "null",
            },
            status=status.HTTP_200_OK
        )
