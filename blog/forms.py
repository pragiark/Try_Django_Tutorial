from django import forms

from models import Article

class ModelForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.Textarea()
    activate = forms.BooleanField()
    
    class Meta:
        model = Article
        fields = [
            'title',
            'content'
        ]
