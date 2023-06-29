from django import forms

from todoapp.models import Task


class Taskform(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']