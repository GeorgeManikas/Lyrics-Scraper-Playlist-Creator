from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(max_length=30,widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder': 'Enter song\'s title'   
    }))
    artist = forms.CharField(max_length=30,widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder': 'Enter song\'s artist'   
    }))