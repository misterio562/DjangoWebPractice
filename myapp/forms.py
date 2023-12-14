from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Título de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'input'}), label="Descripción de tarea", required=False)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyecto", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))    