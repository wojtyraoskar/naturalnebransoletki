# shop/forms.py

from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'email',
            'address', 'postal_code', 'city'
        ]
        widgets = {
            'first_name':  forms.TextInput(attrs={
                'placeholder': 'Imię',
                'class': 'w-full rounded-full border border-[#E7DFD8] px-4 py-3 bg-white/70 backdrop-blur-sm focus:ring-2 focus:ring-[#C8A97E] outline-none transition'
            }),
            'last_name':  forms.TextInput(attrs={
                'placeholder': 'Nazwisko',
                'class': 'w-full rounded-full border border-[#E7DFD8] px-4 py-3 bg-white/70 backdrop-blur-sm focus:ring-2 focus:ring-[#C8A97E] outline-none transition'
            }),
            'email':      forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'w-full rounded-full border border-[#E7DFD8] px-4 py-3 bg-white/70 backdrop-blur-sm focus:ring-2 focus:ring-[#C8A97E] outline-none transition'
            }),
            'address':    forms.TextInput(attrs={
                'placeholder': 'Ulica i numer',
                'class': 'w-full rounded-full border border-[#E7DFD8] px-4 py-3 bg-white/70 backdrop-blur-sm focus:ring-2 focus:ring-[#C8A97E] outline-none transition'
            }),
            'postal_code': forms.TextInput(attrs={
                'placeholder': 'Kod pocztowy',
                'class': 'w-full rounded-full border border-[#E7DFD8] px-4 py-3 bg-white/70 backdrop-blur-sm focus:ring-2 focus:ring-[#C8A97E] outline-none transition'
            }),
            'city':       forms.TextInput(attrs={
                'placeholder': 'Miasto',
                'class': 'w-full rounded-full border border-[#E7DFD8] px-4 py-3 bg-white/70 backdrop-blur-sm focus:ring-2 focus:ring-[#C8A97E] outline-none transition'
            }),
        }
