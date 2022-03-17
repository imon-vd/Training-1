from django.urls import path
from userdata import views

app_name = 'userdata'
# setting this variable in urls helps us do reverse lookups
# in jinja using {% url '' %} along with name variable in path.


urlpatterns = [
    path('',views.formdata,name='formdata'),    
]