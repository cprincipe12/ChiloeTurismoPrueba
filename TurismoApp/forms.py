from django import forms

regiones=(('Tarapaca', 'Tarapaca'), ('Antofagasta', 'Antofagasta'), 
('Atacama', 'Atacama'), ('Coquimbo', 'Coquimbo'), ('Valparaiso', 'Valparaiso'),
('OHiggins', 'OHiggins'), ('Maule', 'Maule'), ('Concepcion', 'Concepcion'), 
('Araucania', 'Araucania'), ('Los Lagos', 'Los Lagos'), ('Aysen', 'Aysen'), 
('Magallanes', 'Magallanes'), ('Metropolitana', 'Metropolitana'), 
('Los Rios', 'Los Rios'), ('Arica', 'Arica'), ('Ñuble', 'Ñuble'), )

class registrarP(forms.Form):
    Rut = forms.CharField(widget=forms.TextInput(),label="Rut")
    Contraseña = forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    Nombre = forms.CharField(widget=forms.TextInput(),label="Nombre")
    ApellidoPaterno = forms.CharField(widget=forms.TextInput(),label="Apellido Paterno")
    ApellidoMaterno = forms.CharField(widget=forms.TextInput(),label="Apellido Materno")
    FechaNacimiento = forms.DateField(widget=forms.SelectDateWidget(years=range(1910,2019)),label="Fecha Nacimiento")
    Correo = forms.EmailField(label="Correo") 
    Telefono = forms.CharField(widget=forms.TextInput(),label="Telefono")
    Region = forms.ChoiceField(choices=(regiones),label="Region")
    Ciudad = forms.CharField(widget=forms.TextInput(),label="Ciudad")

class registrarAdmin(forms.Form):
    Rut = forms.CharField(widget=forms.TextInput(),label="Rut")
    Contraseña = forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    Nombre = forms.CharField(widget=forms.TextInput(),label="Nombre")
    ApellidoPaterno = forms.CharField(widget=forms.TextInput(),label="Apellido Paterno")
    ApellidoMaterno = forms.CharField(widget=forms.TextInput(),label="Apellido Materno")
    FechaNacimiento = forms.DateField(widget=forms.SelectDateWidget(years=range(1910,2019)),label="Fecha Nacimiento")
    Correo = forms.EmailField(label="Correo") 
    Telefono = forms.CharField(widget=forms.TextInput(),label="Telefono")
    Region = forms.ChoiceField(choices=(regiones),label="Region")
    Ciudad = forms.CharField(widget=forms.TextInput(),label="Ciudad")
    TipoUsuario = forms.ChoiceField(choices=(('Usuario', 'Usuario'),('Administrador','Administrador'),),label="Tipo de Usuario")

     
class formularioLogin(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Rut de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")

class registrarLugar(forms.Form):
    Imagen = forms.ImageField(label="Foto del Lugar")
    Nombre = forms.CharField(widget=forms.TextInput(),label="Nombre")
    Descripcion = forms.CharField(widget=forms.TextInput(),label="Descripcion")
    Direccion = forms.CharField(widget=forms.TextInput(),label="Direccion")
    Correo = forms.EmailField(label="Correo")
    Telefono = forms.CharField(widget=forms.TextInput(),label="Telefono")

# Formulario para Email Restablece Contraseña
class RecuperacionForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre de Usuario")

# Formulario para Restablecer Contraseña
class RestablecerForm(forms.Form):
    password_A=forms.CharField(widget=forms.PasswordInput(),label="Nueva Contraseña")
    password_B=forms.CharField(widget=forms.PasswordInput(),label="Repita Contraseña")