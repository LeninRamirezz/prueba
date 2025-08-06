from django.db import models
from ckeditor.fields import RichTextField



class Alumnos(models.Model): #define la estructura de la tabla
    matricula = models.CharField(max_length=12, verbose_name="Mat") #texto corto    #verbose_name: cambia los nombres de los campos
    nombre = models.TextField() #texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    imagen = models.ImageField(null = True, upload_to="foto", verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True) #fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:  #cambia el titulo del modelo y da un ordenamiento a los registros
        verbose_name="Alumno"
        verbose_name_plural="Alumnos"
        ordering=["-created"]   #el menos indica que se ordenará del más reciente al más viejo

    
    def __str__(self):
        return self.nombre #indica que se mostrar el nombre como valor en la tabla
    


class Comentario(models.Model):
    id=models.AutoField(primary_key=True, verbose_name="Clave")
    alumno=models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name="Alumno")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    coment=RichTextField(verbose_name="Comentario")

    class Meta:  #cambia el titulo del modelo y da un ordenamiento a los registros
        verbose_name="Comentario"
        verbose_name_plural="Comentarios"
        ordering=["-created"]   #el menos indica que se ordenará del más reciente al más viejo
    
    def __str__(self):
        return self.coment #indica que se mostrar el nombre como valor en la tabla
    


class ComentarioContacto(models.Model):
    id=models.AutoField(primary_key=True, verbose_name="Clave")
    usuario=models.TextField(verbose_name="Usuario")
    mensaje=models.TextField(verbose_name="Comentario")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Registrado")

    class Meta:
        verbose_name="Comentario Contacto"
        verbose_name_plural="Comentarios Contacto"
        ordering=["-created"]   #el menos indica que se ordenará del más reciente al más viejo
    
    def __str__(self):
        return self.mensaje #indica que se mostrar el nombre como valor en la tabla

class Archivos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    archivo = models.FileField(upload_to="archivos",
                               null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name ="Archivo"
        verbose_name_plural = "Archivos"
        ordering = ["-created"]

    def __str__(self):
        return self.titulo
        

