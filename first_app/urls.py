from django.conf.urls import url
from first_app import views


app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^users/', views.users, name = 'users'),
    url(r'^formshow/',views.formshow,name ='formshow')
]