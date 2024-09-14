from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexvView.as_view(), name='index'),
    # path("", views.index, name='index'),
    path("pitchdeck/", views.pitchdeck, name="pitchdeck")
]
