from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("pitchdeck/", views.pitchdeck, name="pitchdeck")
]
