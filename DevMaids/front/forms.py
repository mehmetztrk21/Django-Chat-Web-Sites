from django import forms
from .models import front


class ChatForm(forms.ModelForm):

    class Meta:
        model = front
        fields = ('message', )
        
