# Generated by Django 2.2.7 on 2019-11-13 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Imagen', models.ImageField(default='static/img_lugares/noname.jpg', upload_to='static/img_lugares')),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=100)),
                ('Correo', models.EmailField(max_length=25)),
                ('Telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Nombre', models.CharField(max_length=15)),
                ('ApellidoPaterno', models.CharField(max_length=15)),
                ('ApellidoMaterno', models.CharField(max_length=15)),
                ('Rut', models.CharField(max_length=15)),
                ('FechaNacimiento', models.CharField(max_length=123)),
                ('Correo', models.EmailField(max_length=25)),
                ('Telefono', models.CharField(max_length=10)),
                ('Region', models.CharField(max_length=50)),
                ('Ciudad', models.CharField(max_length=50)),
            ],
        ),
    ]
