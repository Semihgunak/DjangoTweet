from django.urls import path
from . import views

app_name="template_app"


urlpatterns = [
    path('', views.index, name="index"),
    path("weather/",views.weather_view,name="weatherview"),
    path("index/",views.database,name="databaseview"),
    path("addtweet/",views.addtweet,name="addtweet"),
    path("listtweet/",views.listtweet,name="listtweet"),
    path("addtweetbyform/",views.addtweetbyform,name="addtweetbyform"),
    path("addtweetbymodelform/",views.addtweetbymodelform,name="addtweetbymodelform"),
    path("register/",views.Register.as_view(),name="register"),
    path("deletetweet/<int:id>",views.deletetweet,name="deletetweet"),
]
