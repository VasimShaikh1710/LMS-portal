from django.urls import path
from LMS import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('qrscan/', views.qrscan, name = 'qrscan'),
    path('bionic_hand/', views.bionic_hand, name = 'bionic_hand'),
    #path('home1/', views.home1, name = 'home1'),
    
    path('aster_robot/', views.aster_robot, name = 'aster_robot'),
    #path('home1/', views.home1, name = 'home1'),
    
    path('buybionicpage/login/', views.login, name = 'buy_login'),
    path('buybionicpage/', views.buybionicpage, name = 'buybionicpage'),
    path('logout', views.logout, name='logout'),
    path('base/', views.base, name='base'),
    path('profile/', views.profile, name='profile'),
    path('chat/', views.chat, name='chat'),
    ]