# Generated by Django 4.2.3 on 2023-08-04 12:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('img', models.ImageField(default='/images/cat_default.png', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('due_date', models.DateTimeField(default=datetime.datetime(2023, 8, 5, 12, 7, 6, 411067))),
                ('status', models.CharField(choices=[('F', 'F'), ('O', 'O')], default='O', max_length=1)),
                ('file', models.FileField(blank=True, upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaskApp.category')),
                ('tags', models.ManyToManyField(to='TaskApp.tag')),
            ],
        ),
    ]