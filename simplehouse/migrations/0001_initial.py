# Generated by Django 5.2 on 2025-06-01 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('regid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('status', models.IntegerField()),
                ('role', models.CharField(max_length=10)),
                ('info', models.CharField(max_length=50)),
            ],
        ),
    ]
