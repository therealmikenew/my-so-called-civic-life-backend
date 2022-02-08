from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('user/', views.UserList.as_view(), name='user'),
    path('legislation/<int:pk>', views.LegislationDetail.as_view(),
         name='legislation_detail'),
    path('action/<int:pk>', views.ActionDetail.as_view(),
         name='action_detail'),
    path('user/<int:pk>', views.UserList.as_view(), name='user_detail')

]
