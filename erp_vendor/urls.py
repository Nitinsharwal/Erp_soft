from django.urls import path,include
from erp_vendor import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('vendor_api',views.vendorViewSet,basename='vendor_api')
urlpatterns = [
    path('home', views.home, name="home"),
    path('', include(router.urls)),
    path('vendor_erp', views.vendor_page, name="vendor_erp"),
]