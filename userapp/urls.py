
# from django.contrib import admin
from django.urls import path,include
from userapp.views import *
# from userapp.views import CustomerViewSet
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'customer',CustomerViewSet)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('create',Customerview),
     path('login',LoginView),
      path('product',ProductView ,name='product_view'),
        #   path('product?<int:p_id>', ProductView, name='product_detail'),  # <int:p_id> captures the p_id parameter

]
