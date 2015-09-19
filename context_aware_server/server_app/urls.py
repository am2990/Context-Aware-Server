from django.conf.urls import url
from server_app import views

urlpatterns = [
    url(r'^store/$', views.store, name="store"),
]