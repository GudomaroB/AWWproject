from django.urls import path, include
from .views import (
    IndexView, OnlineShopView, EnterprisePortalView, BCView, LPView, PortalView, PromoView, PricesView, ContactCreateView
)

app_name = 'contacts'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('online_shop/', OnlineShopView.as_view(), name='online_shop'),
    path('enterprise/', EnterprisePortalView.as_view(), name='enterprise_portal'),
    path('landing/', LPView.as_view(), name='landing'),
    path('portal/', PortalView.as_view(), name='portal'),
    path('prices/', PricesView.as_view(), name='prices'),
    path('promo/', PromoView.as_view(), name='promo'),
    path('business_card/', BCView.as_view(), name='vizitka'),
    path('contact/', ContactCreateView , name='contact_form'),
]
