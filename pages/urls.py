from django.urls import path
from . import views # import views from the same directory



urlpatterns = [
    
    
    path('', views.index, name='index'),
    path('actu', views.actu, name='actu'),
    path('cont', views.cont, name='cont'),
    path('<int:project_id>', views.detail, name='detail'),
    path('about', views.about, name='about'),
    
]