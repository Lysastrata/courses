from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^remove/(?P<course_id>\d+)$', views.remove)
]
