from django.urls import path
from . import views
app_name='finalapp'
urlpatterns = [

    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('abc/',views.abc,name='abc'),
    path('details/',views.details,name='details'),
    path('final/',views.final,name='final')
]