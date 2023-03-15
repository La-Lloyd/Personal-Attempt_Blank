from django import forms

class FormName(form.Form):
    name = forms.CharField()
    email = forms.EmailField()
    test = forms.CharField(widget=forms.textarea)