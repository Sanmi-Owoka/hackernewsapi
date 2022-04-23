from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from ..serializers.delete_serializer import DeleteSerializer
from news.models import News


class DeleteNewsView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = DeleteSerializer

    def delete(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "message": "Failure",
                    "errors": serializer.errors,
                    "data": "null"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        id = serializer.validated_data["id"]
        try:
            news = News.objects.get(is_from_api=False, id=id)
            news.delete()
            return Response(
                {
                    "message": "News successfully deleted",
                },
                status=status.HTTP_204_NO_CONTENT
            )
        except ObjectDoesNotExist:
            return Response(
                {
                    "message": "Failure",
                    "errors": "These News does exist",
                    "data": "null"
                },
                status=status.HTTP_404_NOT_FOUND
            )
