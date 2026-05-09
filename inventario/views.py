from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):
pathroductos = producto.objects.all()
return render(request, 'inventario/lista.html', {'productos': productos})
@login_required  # Protección nativa (Pág. 9 presentación)
def crear_producto(request):
	if request.method == 'POST':
	form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('lista_productos')
	else:
		form = ProductoForm()
	return render(request, 'inventario/formulario.html', {'form': form})