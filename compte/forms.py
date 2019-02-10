from django import forms

class ContactForm(forms.Form):
    name = forms.EmailField(
        label='login',
        max_length=100,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
        )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
required=True)