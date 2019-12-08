# Generated by Django 2.2.7 on 2019-11-13 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TurismoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='TipoUsuario',
            field=models.CharField(default='Usuario', max_length=50),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='Imagen',
            field=models.ImageField(default='TurismoApp\\static\\img_lugares\noname.jpg', upload_to='TurismoApp\\static\\img_lugares'),
        ),
    ]
