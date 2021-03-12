from django import forms
from .models import Chatt


class ChatForm(forms.ModelForm):

    class Meta:
        model = Chatt
        fields = ('message', )
        
