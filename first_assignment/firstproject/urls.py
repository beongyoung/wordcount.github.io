from django.contrib import admin
from django.urls import path
import wordcount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount.views.home, name="base"),
    path('about/', wordcount.views.about, name="about"),
    path('result/', wordcount.views.result, name="result"),
    path('blank/', wordcount.views.blank, name="blank"),
]