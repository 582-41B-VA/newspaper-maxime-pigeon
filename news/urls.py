from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:id>/", views.article, name="article"),
    path("<int:id>/comment", views.comment, name="comment"),
]
