from django.urls import path
from . import views

urlpatterns = [
    path('users/register/', views.register_user, name='register_user'),
    path('users/login/', views.login_user, name='login_user'),
    path('patients/', views.add_patient, name='add_patient'),
    path('patients/<int:user_id>/', views.get_patients, name='get_patients'),
    path('heart_rates/', views.record_heart_rate, name='record_heart_rate'),
    path('heart_rates/<int:patient_id>/', views.get_heart_rates, name='get_heart_rates'),
]