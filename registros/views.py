from django.shortcuts import render
from .models import Alumnos   #Accedemos la modelo alumno que contiene la estructura de la tabla
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
import datetime
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages


def registros (request):
    alumnos=Alumnos.objects.all() #all recupera todos los objetos del modelo(registros de la tabla alumnos)
    return render(request, "registros/principal.html",{'alumnos':alumnos})
    #Indicamos el lugar donde se renderiza el resultado de esta vista y enviamos la lista de alumnos recuperados


def registrar(request):
    if request.method == 'POST':
        form=ComentarioContactoForm(request.POST)
        if form.is_valid():  #si los datos recibidos son correctos
            form.save()  #inserta
            return render (request, 'registros/contacto.html')
    form=ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulariolos datos ingresados
    return render(request, 'registros/contacto.html', {'form':form})


def contacto(request):
    return render(request, "registros/contacto.html")
    #Indicamos el lugar donde se realizara el resultado de esta vista

def Comentarios(request):
    comentarios=ComentarioContacto.objects.all() #all recupera todos los objetos del modelo(registros de la tabla alumnos)
    return render(request, "registros/ConsultaComentarios.html",{'comentarios':comentarios})


def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    return render(request,"registros/formEditarComentario.html", {'comentario': comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/consultaComentarios.html", {'comentarios': comentarios})
    return render (request,"registros/formEditarComentario.html",{'comentario':comentario} )

def eliminarComentarioContacto(request,id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto,id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultaContacto.html", {'comentario':comentarios})
    return render(request, confirmacion, {'object':comentario})

def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan","Ana"])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2025, 7,9)
    fechaFin = datetime.date(2025, 7, 9)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar8(request):
    fechaInicio = datetime.date(2025,7,8)
    fechaFin = datetime.date(2025,7,9)
    comentariosContacto = ComentarioContacto.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/Comentarios_consulta.html",{'comentarios':comentariosContacto})

def consultar9(request):
    comentariosContacto = ComentarioContacto.objects.filter(mensaje__contains='Reprobado')
    return render(request,"registros/Comentarios_consulta.html",{'comentarios':comentariosContacto})

def consultar10(request):
    comentariosContacto = ComentarioContacto.objects.filter(usuario__in=["Azharel Perez"])
    return render(request,"registros/Comentarios_consulta.html",{'comentarios':comentariosContacto})

def consultar11(request):
    comentariosContacto = ComentarioContacto.objects.only("mensaje")
    return render(request,"registros/Comentarios_consulta.html",{'comentarios':comentariosContacto})

def consultar12(request):
    comentariosContacto = ComentarioContacto.objects.filter(usuario__icontains="z")
    return render(request, "registros/Comentarios_consulta.html", {'comentarios': comentariosContacto})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request, "registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request, "registros/archivos.html", {'archivo': Archivos})

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html", {'alumnos':alumnos})

def seguridad(request, nombre="None"):
    nombre= request.GET.get('nombre')
    return render(request,"registros/seguridad.html", {'nombre':nombre})