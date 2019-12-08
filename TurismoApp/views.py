from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader

# Imports para Cosas de Sesión (Login)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Correos
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password

# Al crear cada formulario nuevo, Agregarlo a esta línea
from .forms import registrarP, registrarAdmin, formularioLogin, registrarLugar, RecuperacionForm, RestablecerForm
# -----------------------------------------

# Al agregar una nueva tabla a la base de datos, agregarla a esta línea
from .models import Usuario, Lugar
# ------------------------------------
# Create your views here.

def index(request):
    plantilla=loader.get_template("index.html")
    return HttpResponse(plantilla.render({'titulo':'Chiloe Turismo'},request))

def quienessomos(request):
    plantilla=loader.get_template("quienessomos.html")
    return HttpResponse(plantilla.render({'titulo':'Chiloe Turismo'},request))

def registroPersona(request):
    mensaje=""
    registro=1
    form=registrarP(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        new=User.objects.create_user(data.get("Rut"), data.get("Correo"), data.get("Contraseña"))
        new.is_staff=False
        new.save()
        regDB=Usuario(Usuario=new,Nombre=data.get("Nombre"),ApellidoPaterno=data.get("ApellidoPaterno"),
        ApellidoMaterno=data.get("ApellidoMaterno"),Rut=data.get("Rut"), FechaNacimiento=data.get("FechaNacimiento"),
        Correo=data.get("Correo"),Telefono=data.get("Telefono"),Region=data.get("Region"),
        Ciudad=data.get("Ciudad"))
        regDB.save()
        mensaje='Usuario '+regDB.Nombre+' Registrado'
    form=registrarP()
    return render(request,"formulario.html",{'form':form,'titulo':"Formulario",'registro':registro})

@login_required(login_url='login')
def registroAdmin(request):
    actual=request.user
    mensaje=""
    registro=2 # Dependiendo este Numero es el Formulario que Mostrará
    form=registrarAdmin(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        new=User.objects.create_user(data.get("Rut"), data.get("Correo"), data.get("Contraseña"))
        # Tipo es Tomado del Formulario (El ComboBox/ChoiceField)
        tipo = data.get("tipoPersona") # Lo Guardo en una Variable para evitar posibles Problemas
        if tipo == 'Usuario': # Verifica el Texto tomado del ComboBox/ChoiceField
            new.is_staff=False # El is_staff es un campo que viene con la clase USER, es para diferenciar los tipos de usuario,
            # SI es un usuario normal, queda en False
        else:
            # Pero si tiene como Tipo "Admnistrador", queda en True. Gracias a esto puedes hacer la diferencia en el HTML Maqueta
            new.is_staff=True
        new.save() # IMPORTANTE PONERLE SAVE Y RECORDAR QUE LOS USUARIOS CREADOS DESDE QUE EDITAS ESTO SON LOS QUE TENDRAN LOS PRIVILEGIOS DE Admin
        regDB=Usuario(Usuario=new,Nombre=data.get("Nombre"),ApellidoPaterno=data.get("ApellidoPaterno"),
        ApellidoMaterno=data.get("ApellidoMaterno"),Rut=data.get("Rut"), FechaNacimiento=data.get("FechaNacimiento"),
        Correo=data.get("Correo"),Telefono=data.get("Telefono"),Region=data.get("Region"),
        Ciudad=data.get("Ciudad"),TipoUsuario=data.get("TipoUsuario"))
        regDB.save()
        mensaje='Usuario '+regDB.Nombre+' Registrado'
    form=registrarAdmin()
    return render(request,"formulario.html",{'form':form,'actual':actual,'registro':registro,'titulo':"Registro",'mensaje':mensaje})



@login_required(login_url='login')
def registroLugar(request):
    actual=request.user
    mensaje=""
    form=registrarLugar(request.POST, request.FILES)
    if form.is_valid():
        data=form.cleaned_data
        regDB=Lugar(Imagen=data.get("Imagen"),Nombre=data.get("Nombre"),Descripcion=data.get("Descripcion"),Direccion=data.get("Direccion"),Correo=data.get("Correo"),Telefono=data.get("Telefono"))
        regDB.save()
        mensaje='Lugar '+regDB.Nombre+' Registrado'
    form = registrarLugar()
    return render(request, "registroLugar.html", {'form': form, 'actual':actual,'titulo':"Registro Lugar",'mensaje':mensaje})


def lugares(request):
    actual=request.user
    lugars=Lugar.objects.all()
    return render (request,"lugares.html",{'lugars':lugars,'actual':actual,'titulo':"Lista de Lugares",})

def personas(request):
    actual=request.user
    people=Usuario.objects.all()
    return render (request,"personas.html",{'people':people,'actual':actual,'titulo':"Lista de Lugares",})


def ingreso(request):
    mensaje=""
    form=formularioLogin(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            mensaje='Datos Invalidos'
    return render(request,"login.html",{'form':form,'titulo':"Login",'mensaje':mensaje})

def salir(request):
    logout(request)
    return redirect('/index/')

def borrarLugar(request, postid):
    objeto=Lugar.objects.filter(Codigo=postid)
    objeto.delete()
    return redirect("/lugares/")

# Recuperacion Contraseña
def olvido(request):
    form=RecuperacionForm(request.POST or None)
    mensaje=""
    if form.is_valid():
        data=form.cleaned_data
        user=User.objects.get(username=data.get("username"))
        send_mail(
                'Recuperación de contraseña',
                'Haga click aquí para ingresar una nueva contraseña',
                'chiloeturismo.duoc@gmail.com',
                [user.email],
                html_message = 'Pulse <a href="http://localhost:8000/restablecer?user='+user.username+'">aquí</a> para restablecer su contraseña.',
            )
        mensaje='Correo Enviado a '+user.email
    return render(request,"olvido.html",{'form':form, 'mensaje':mensaje, 'titulo':"Recuperar Contraseña",})

# Restablecer Contraseña
def restablecer(request):
    form=RestablecerForm(request.POST or None)
    mensaje=""
    try:
        username=request.GET["user"]
    except Exception as e:
        username= None
    if username is not None:
        if form.is_valid():
            data=form.cleaned_data
            if data.get("password_A") == data.get("password_B"):
                mensaje="La contraseña se ha restablecido"
                contra=make_password(data.get("password_B"))
                User.objects.filter(username=username).update(password=contra)
            else:
                mensaje="Las contraseñas no coinciden"
        return render(request,"restablecer.html",{'form':form, 'username':username, 'mensaje':mensaje, 'titulo':"Restablecer Contraseña",})
    else:
        return redirect('/login/')
