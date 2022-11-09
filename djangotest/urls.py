from django.urls import path
from myapp import views
urlpatterns = [
    # define a route for home
    path('', views.home, name='home'),
    path('webhook/', views.webhook, name='webhook'),
    path('ans', views.result, name = 'result' )
  
]