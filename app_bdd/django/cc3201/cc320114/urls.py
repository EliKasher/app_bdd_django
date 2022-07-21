from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('main1/', views.main1),
    path('main2/', views.main2),
    path('main3/', views.main3),
    path('main4/', views.main4),
    path('main5/', views.main5),
    path('consulta1/', views.consulta1),
    path('consulta2/', views.consulta2),
    path('consulta3/', views.consulta3),
    path('consulta4/', views.consulta4),
    path('consulta5/', views.consulta5)
]