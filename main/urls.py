from django.urls import path
from . import views

urlpatterns = [
    # front
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # team
    path('dashboard/team/create/', views.create_team, name='create_team'),
    path('dashboard/team/list/', views.teams, name='teams'),
    path('dashboard/team/update/<int:id>/', views.team_update, name='team_update'),
    path('dashboard/team/delete/<int:id>/', views.team_delete, name='team_delete'),
    # itms
    path('dashboard/works/create/', views.work_create, name='work_create'),
    path('dashboard/works/list/', views.works, name='works'),
    path('dashboard/works/update/<int:id>/', views.work_update, name='work_update'),
    path('dashboard/works/delete/<int:id>/', views.work_delete, name='work_delete'),
    # murojatlar
    path('dashboard/appeal/list/', views.appeal_dashboard, name='appeal_dashboard'),
    path('dashboard/appeal/delete/<int:id>/', views.appeal_delete, name='appeal_delete'),
    path('auth/register/', views.register_user, name='register_user'),
    path('auth/login/', views.login1, name='login'),
    path('auth/log_out/', views.log_out, name='log_out')
]