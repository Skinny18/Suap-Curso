from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label= 'Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    