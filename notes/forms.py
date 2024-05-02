from django import forms

from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['text', 'title']
        labels = {
            'text': 'Write your thoughts:'
        }
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'title': forms.Textarea(attrs={'class': 'form-control mb-5'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('Now we only accept notes about Django')
        return title
