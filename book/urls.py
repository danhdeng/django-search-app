from django.urls import path, include
from .views import post_search_view

app_name = "book"

urlpatterns = [path("search/", post_search_view, name="search")]
