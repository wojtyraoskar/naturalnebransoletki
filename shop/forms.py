from django import forms

class CheckoutForm(forms.Form):
    name = forms.CharField(label="Imię i nazwisko", max_length=100)
    email = forms.EmailField(label="Email")
