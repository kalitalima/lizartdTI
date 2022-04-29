from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postagem', views.cadastro_postagem, name='postagem'),
    path('inscrever', views.cadastro_inscricao, name='inscrever')
]
