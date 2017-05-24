from django.conf.urls import url
from farm_app import views


app_name = 'farm_app'


urlpatterns = [
    url(r'^$', views.home, name='home'),
]
