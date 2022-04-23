from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from ..serializers.get_and_post_serializer import NewsSerializer, GetNews
from news.models import News


class NewsView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {
                    "message": "Success",
                    "data": serializer.data,
                    "errors": "null"
                }
            )
        return Response(
            {
                "message": "Failure",
                "errors": serializer.errors,
                "data": "null"
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request):
        news = News.objects.all()
        if news:
            serializer = GetNews(news, many=True)
            return Response(
                {
                    "message": "Success",
                    "data": serializer.data,
                    "errors": "null"
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                "message": "Failure",
                "data": "No news",
                "errors": "null",
            },
            status=status.HTTP_404_NOT_FOUND
        )
