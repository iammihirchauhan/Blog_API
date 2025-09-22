from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogPostListCreate.as_view(), name="blogpostview"),
    path("<int:pk>", views.BlogPostRetrieveUpdateDestroy.as_view(), name="update"),

]
