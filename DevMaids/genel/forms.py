from django import forms
from .models import genel


class ChatForm(forms.ModelForm):

    class Meta:
        model = genel
        fields = ('message', )
        
