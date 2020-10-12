from django import forms
from .models import Evaluations
from captcha.fields import CaptchaField


class EvaluationsForm(forms.ModelForm):
    captcha = CaptchaField()

    photos = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Evaluations
        fields = ['name', 'contact', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }