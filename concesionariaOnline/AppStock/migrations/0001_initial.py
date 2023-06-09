# Generated by Django 4.2 on 2023-04-29 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asesoramiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('telefono', models.IntegerField()),
                ('dataDeAsesoramiento', models.CharField(max_length=250)),
                ('modeloDelAuto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsuario', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='autos')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('año', models.IntegerField()),
                ('kilometros', models.IntegerField()),
                ('descripcion', models.CharField(max_length=250)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(null=True, upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
