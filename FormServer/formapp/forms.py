from django import forms

from .models import FormModel


class FormForm(forms.ModelForm):

    class Meta:
        model = FormModel
        fields = ('name', 'last_name', 'email', 'phone')
