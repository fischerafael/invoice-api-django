

from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from clients.views import ClientViewset, ClientViewsetDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clients/', ClientViewset.as_view()),   
    path('api/clients/<int:pk>/', ClientViewsetDetail.as_view())
]
