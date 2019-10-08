from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
	path('',views.index,name='index'),
	path('login/', auth_views.LoginView.as_view(template_name='Clono/registration/login.html'), name="login"),
	path('logout/', auth_views.LogoutView.as_view(template_name='Clono/logout.html'),name='logout'),
	path('register/',views.register,name='register'),
	path('myAccount/',views.myAccount,name='myAccount'),
	path('to_apply/',views.to_apply,name='to_apply'),
	path('customerMain/',views.customerMain,name='customerMain'),
	path('to_apply/calculate',views.calculate,name='calculate'),
	path('to_apply/cloudcomputing/',views.cloudcomputing,name='cloudcomputing'),
	path('to_apply/Pythonpart/',views.Pythonpart,name='Pythonpart'),
	path('to_apply/Webdevelopment/',views.Webdevelopment,name='Webdevelopment')

]
