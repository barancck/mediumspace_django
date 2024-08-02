from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='Home MediumAI'),
    path("pitchdeck/", views.pitchdeck, name="pitchdeck")
]
