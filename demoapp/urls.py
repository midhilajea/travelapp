
from . import views
from django.urls import path

from . import views
from django.urls import path
app_name='demoapp'

urlpatterns = [
    path('',views.home,name='home'),

]