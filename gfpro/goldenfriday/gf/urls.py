from django.conf.urls import url

from . import views
from gf.views import home
urlpatterns = [
    url(r'^$',home, name='home'),
]