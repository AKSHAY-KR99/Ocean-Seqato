from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'lead', views.LeadsViewSet)
router.register(r'contact', views.ContactAddViewSet)


urlpatterns = [
    path('countries/', views.ListCountries.as_view(), name='list_countries'),
    path('currencies/', views.ListCurrencies.as_view(), name='list_currencies'),
    path('lead/status/<slug:admin_action>/', views.ApproveLeadStatusView.as_view(), name='approve_lead_data'),
    path('email/check/', views.EmailExistenceCheck.as_view(), name='check_email_existence'),
    path('phone_number/check/', views.PhoneNumberExistenceCheck.as_view(), name='check_phone_number_existence'),
    path('', include(router.urls)),
]
