# Generated by Django 4.2.5 on 2023-09-21 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Korxona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(default='', max_length=202)),
                ('detail', models.TextField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
