from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario (models.Model):
    Usuario=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    Nombre = models.CharField(max_length=15)
    ApellidoPaterno = models.CharField(max_length=15)
    ApellidoMaterno = models.CharField(max_length=15)
    Rut = models.CharField(max_length=15)
    FechaNacimiento = models.CharField(max_length=123)
    Correo = models.EmailField(max_length=25)
    Telefono = models.CharField(max_length=10)
    Region = models.CharField(max_length=50)
    Ciudad = models.CharField(max_length=50)
    TipoUsuario = models.CharField(max_length=50, default='Usuario')

    def __str__(self):
        return self.Nombre +' '+ self.ApellidoPaterno +' '+ self.ApellidoMaterno


class Lugar (models.Model):
    Codigo = models.AutoField(primary_key=True)
    Imagen = models.ImageField(upload_to='TurismoApp\static\img_lugares', default='TurismoApp\static\img_lugares\noname.jpg')
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Correo = models.EmailField(max_length=25)
    Telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.Nombre