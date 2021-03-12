from django import forms
from .models import backend


class ChatForm(forms.ModelForm):

    class Meta:
        model = backend
        fields = ('message', )
        
