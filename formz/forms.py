from django import forms

class NameForm(forms.Form):
    you1ame = forms.CharField(label='Введите ID ЖК', max_length=6)
