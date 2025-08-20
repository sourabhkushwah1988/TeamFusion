from django.urls import path
from.import views
urlpatterns = [
    path('',views.index),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('signinpage',views.signinpage,name='signinpage'),
    path('userhome',views.userhome,name='userhome'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('view_team', views.view_team, name='view_team'),
    path('logout',views.logout,name='logout'),
    path('my_profile', views.my_profile, name='my_profile'),
    
    ]
