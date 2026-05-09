from django import forms 
froms .models import Producto

class ProductoForm(forms.Form):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio','stock','categoria']