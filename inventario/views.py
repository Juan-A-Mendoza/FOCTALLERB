from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from .model import Producto
from .forms import ProductoForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/lista.html', {'productos': productos})
    @login_required # Proteccion nativa

    def crear_producto(request):
        if request.method == 'POST':
            form = ProductoForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("lista_productos")
            else:
                form = ProductoForm()
            return render(request, 'inventario/formulario.html',{'form':form})  