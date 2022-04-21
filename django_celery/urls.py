from django.contrib import admin
from django.urls import path
from apps.core.views import home
from apps.produtos.views import UpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('editar/<int:pk>/', UpdateView.as_view(), name='editar')
]
