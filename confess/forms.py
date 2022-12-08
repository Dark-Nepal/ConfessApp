from django import forms
from confess.models import confess

class ConfessForm(forms.ModelForm):
    class Meta:
        model = confess
        fields = ['confession']
        
    def __init__(self, *args, **kwargs):
         super(ConfessForm, self).__init__(*args, **kwargs)
         self.fields['confession'].widget.attrs['placeholder'] = 'Write your confession...'
         self.fields['confession'].widget.attrs['class'] = 'form-control'
         self.fields['confession'].widget.attrs['style'] = 'height: 200px'


        