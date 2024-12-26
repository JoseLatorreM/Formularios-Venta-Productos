from django.shortcuts import render, redirect
from AplicacionRecu.models import Compra
from django.shortcuts import render, get_object_or_404
# Create your views here.

def VistaCompras(request):
    SacarDatos = Compra.objects.all()
    return render(request, "ListadoVenta.html", {'SacarDatos':SacarDatos})

def Autor(request):
    return render (request, "Autor.html")

def Formulario(request):
    return render (request, "FormularioVenta.html")

def Menu(request):
    return render (request, "Menu.html")

def guardar_datos(request):
        rut = request.POST['Rut']
        producto = request.POST['Producto']
        valorcosto = request.POST['Valor_Costo']
        utilidad = request.POST['Utilidad']
        valorventa = request.POST['Valor_Venta']
        cantidad = request.POST['Cantidad']
        total = request.POST['Total']
        SacarDatos = Compra(
            Rut=rut,
            Producto=producto,
            Valor_Costo=valorcosto,
            Utilidad=utilidad,
            Valor_Venta=valorventa,
            Cantidad=cantidad,
            Total=total
        )
        SacarDatos.save()
        return redirect(VistaCompras)

def buscar_por_pk(request):
    if request.method == 'POST':
        rut = request.POST.get('pk', None)
        if rut is not None:
            objeto = get_object_or_404(Compra, Rut=rut)
            return render(request, 'ModificarDato.html', {'objeto': objeto, 'rut_buscado': rut})
    return render(request, 'error.html') 

def ModificarDato(request, rut):
    if request.method == 'POST':
        rut = request.POST.get('Rut')
        producto = request.POST.get('Producto')
        valor_costo = request.POST.get('Valor_Costo')
        utilidad = request.POST.get('Utilidad')
        valor_venta = request.POST.get('Valor_Venta')
        cantidad = request.POST.get('Cantidad')
        total = request.POST.get('Total')
    # Obtener el objeto existente
        objeto = get_object_or_404(Compra, Rut=rut)
    # Actualizar los campos
        objeto.Producto = producto
        objeto.Valor_Costo = valor_costo
        objeto.Utilidad = utilidad
        objeto.Valor_Venta = valor_venta
        objeto.Cantidad = cantidad
        objeto.Total = total
        objeto.save()
        return redirect(VistaCompras)
    return render(request, 'error.html')  # Maneja el caso de 

def borrar(request,id):
    SacarDatos = Compra.objects.get(id=id)
    SacarDatos.delete()
    return redirect(VistaCompras)    

                   
def home(request):
    return render (request, 'AplicacionRecu/home.html')
    
def products(request):
    return render (request, 'AplicacionRecu/products.html')
