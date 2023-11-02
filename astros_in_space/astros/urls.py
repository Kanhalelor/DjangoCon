from django.urls import path
from . import views

# create a list of URL partens

urlpatterns = [
    # define paths here
    path("", views.astronauts, name="austros"),
]
