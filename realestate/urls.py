from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("buildingShow/<str:id>/",views.buildingShow,name="buildingShow"),
    path("createPost/",views.createPost,name="createPost"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("profile/",views.profile,name="profile"),
]
