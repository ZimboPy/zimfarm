from django.conf.urls import url
from farmer import views


app_name = 'farmer'


urlpatterns = [
    url(r'^$', views.home, name='home'),
]
