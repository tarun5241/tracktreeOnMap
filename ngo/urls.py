
from django.urls import path

from . import views



urlpatterns = [ 
    path('', views.index , name="index" ),
    path('index.html', views.index , name="index" ),
    path('login', views.login1 , name="login" ),
    path('signup/', views.signup , name="signup" ),
    
    path('login-user/', views.loginUser , name="login-user" ),
    path('logout/',views.logoutUser , name='logout'),
    
    path('register/<str:pk>/', views.register , name="register" ),
    path('ngo/<str:pk>/', views.ngoProfile , name="profile" ),
    
    path('create-ngo/<str:pk>/', views.createNgo, name='create-ngo'),
    path('create-user/', views.createUser, name='create-user'),
    
    path('map/<str:pk>/', views.map, name='map'),
    path('create-event/<str:pk>/', views.createEvent , name='create-event'),
    
    path('add-event/<str:pk>/', views.addEvent , name='add-event'),
    path('event/<str:pk>/', views.event , name='event'),
   
]
