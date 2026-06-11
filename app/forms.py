from .models import Content
from django import forms

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "w-full border rounded px-3 py-2 focus:outline-none focus:ring focus:ring-blue-300",
                "placeholder": "Enter title"
            }),

            "img": forms.TextInput(attrs={
                "class": "w-full border rounded px-3 py-2 focus:outline-none focus:ring focus:ring-blue-300",
                "placeholder": "Image URL"
            }),
        }