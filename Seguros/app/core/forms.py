from django import forms
from .models import Cotizador

class CotizadorForm(forms.ModelForm):
    class Meta:
        model = Cotizador
        fields = [
            'customer', 'validity_date', 'term_days', 'expiration_date',
            'policy_type', 'insured_value', 'rate', 'minimum_premium',
            'premium', 'extra_charge', 'fee', 'tax', 'total'
        ]
        widgets = {
            'validity_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'expiration_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'term_days': forms.NumberInput(attrs={'class': 'form-control'}),
            'insured_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'minimum_premium': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'premium': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'extra_charge': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fee': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tax': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'total': forms.TextInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'policy_type': forms.TextInput(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
        }
