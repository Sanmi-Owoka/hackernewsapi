from django.urls import path
from .views.post_and_get_news import NewsView
from .views.update_news import UpdateNewsView
from .views.delete_news_view import DeleteNewsView

urlpatterns = [
    path('news/', NewsView.as_view(), name='get-and-post'),
    path('update-news/', UpdateNewsView.as_view(), name='update'),
    path('delete/', DeleteNewsView.as_view(), name='delete')
]
