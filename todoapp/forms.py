from django import forms
from categorias.models import Categoria
from .models import Tarea


class NuevaTareaForm(forms.Form):
   titulo = forms.CharField(label="titulo de la tarea")
   contenido = forms.CharField(widget=forms.Textarea()) # <textarea> en vez de <input>
   categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())

class NuevaTareaModelForm(forms.ModelForm):
        titulo = forms.CharField(label="Título de la tarea")
        class Meta:
               model = Tarea
               fields = ['titulo', 'contenido', 'categoria']

        def clean_titulo(self):	
               field = self.cleaned_data.get("titulo")
               if not "Tarea" in field:
                       raise forms.ValidationError("Debe incluir el texto 'Tarea'")
               return field