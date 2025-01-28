from django.urls import path
from .views import CotizadorCreateView, insurance_policy_success  # Importa las vistas desde views.py

urlpatterns = [
    path('', CotizadorCreateView.as_view(), name='home'),  # Ruta para la raíz, redirige al formulario de creación
    path('crear-poliza/', CotizadorCreateView.as_view(), name='crear_poliza'),  # Ruta para crear la póliza
    path('exito/', insurance_policy_success, name='insurance_policy_success'),  # Ruta de la página de éxito
]

