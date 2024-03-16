from django.urls import path
from . import views

urlpatterns = [
    # Company URLs
    path('api/companies/', views.company_list_create, name='company-list-create'),
    path('api/companies/<int:pk>/', views.company_detail, name='company-detail'),

    # Employee URLs
    path('api/employees/', views.employee_list_create, name='employee-list-create'),
    path('api/employees/<int:pk>/', views.employee_detail, name='employee-detail'),

    # Device URLs
    path('api/devices/', views.device_list_create, name='device-list-create'),
    path('api/devices/<int:pk>/', views.device_detail, name='device-detail'),

    # DeviceLog URLs
    path('api/device-logs/', views.device_log_list_create, name='device-log-list-create'),
    path('api/device-logs/<int:pk>/', views.device_log_detail, name='device-log-detail'),
]
