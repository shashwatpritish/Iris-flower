from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('flower/',views.flower,name="flower"),
    path('about/',views.about,name="about"),
]
