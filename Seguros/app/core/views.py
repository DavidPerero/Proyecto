from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Cotizador
from .forms import CotizadorForm

# Vista basada en clases para crear la póliza
class CotizadorCreateView(CreateView):
    model = Cotizador
    form_class = CotizadorForm  # Usar el formulario personalizado
    template_name = 'Cotizador.html'  # Ruta de la plantilla del formulario
    success_url = reverse_lazy('insurance_policy_success')  # Redirige a la URL de éxito

# Vista para mostrar la página de éxito
def insurance_policy_success(request):
    return render(request, 'success.html')

