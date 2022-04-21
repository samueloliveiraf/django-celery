from django.contrib import admin
from django.urls import path
from apps.core.views import home
from apps.produtos.views import UpdateViewProduct


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('editar/<int:pk>/', UpdateViewProduct.as_view(), name='editar')
]
