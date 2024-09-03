from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('vote/<int:question_id>/', views.vote_view, name='vote'),
    path('results/<int:question_id>/', views.results_view, name='results'),
    path('detail/<int:question_id>/', views.detail_view, name='detail'),

]
