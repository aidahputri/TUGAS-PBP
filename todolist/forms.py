from django import forms

class FormTask(forms.Form):
  title = forms.CharField(label="Title", max_length=100, widget=forms.TextInput(attrs={"class":"inp-title"}))
  description = forms.CharField(label="Description", max_length=300, widget=forms.TextInput(attrs={"class":"inp-description"}))