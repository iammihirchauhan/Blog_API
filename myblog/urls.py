from django.urls import path, include

urlpatterns = [
    path("blogpost/", include("blogapi.urls")),
]
