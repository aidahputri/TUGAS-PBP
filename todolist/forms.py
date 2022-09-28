from django import forms

class FormTask(forms.Form):
  title = forms.CharField(label="Title", max_length=100)
  description = forms.CharField(label="Description", max_length=300)