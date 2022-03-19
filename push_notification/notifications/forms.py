from django import forms

from .models import Promocoes


class PromocoesForm(forms.ModelForm):
    class Meta:
        model = Promocoes
        fields = "__all__"
