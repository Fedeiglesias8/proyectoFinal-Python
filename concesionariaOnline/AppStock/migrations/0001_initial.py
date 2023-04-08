# Generated by Django 4.2 on 2023-04-07 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alquiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=20)),
                ('año', models.IntegerField()),
                ('descripcion', models.CharField(max_length=250)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='asesoramiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('telefono', models.IntegerField()),
                ('dataAsesoramiento', models.CharField(max_length=250)),
                ('modeloAuto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=20)),
                ('año', models.IntegerField()),
                ('kilometros', models.IntegerField()),
                ('descripcion', models.CharField(max_length=250)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]