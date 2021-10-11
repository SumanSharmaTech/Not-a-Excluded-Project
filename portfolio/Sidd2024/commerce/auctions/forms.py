from django import forms
from .models import Listing, category

class create_form(forms.ModelForm):
    
    title=forms.CharField(max_length=64, 
    widget=forms.TextInput(attrs={'placeholder': 'Title'}))

    description=forms.CharField(max_length=200,
    widget=forms.Textarea(attrs={'placeholder': 'Describe your listing'}))

    bid=forms.DecimalField(max_digits=10, decimal_places=2,
    widget=forms.TextInput(attrs={'placeholder': 'Starting Bid'}))

    image=forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Image URL'}))

    category=forms.ModelChoiceField(queryset=category.objects.all(), empty_label='Category')

    class Meta:
        model = Listing
        fields = ['title', 'description', 'bid', 'image', 'category']
