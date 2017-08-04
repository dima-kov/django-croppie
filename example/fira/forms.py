from django import forms
from croppie.fields import CroppieField

from fira.models import Fira


class FiraForm(forms.ModelForm):
    image = CroppieField()

    class Meta:
        model = Fira
        fields = '__all__'
