from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='BlogHome'),
    path("vblogpost/<int:id>", views.vblogpost, name="blogHome")
]