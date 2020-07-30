from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('create/superuser', views.CreateSuperUserView.as_view(), name='createsuperuser'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
]