from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta:
        model = Product
        fields = ['name', 'category', 'company', 'price', 'quantity', 'description']
