# Generated by Django 5.1.7 on 2025-06-03 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ME_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mnm', models.CharField(max_length=25)),
                ('prc', models.IntegerField()),
                ('im', models.FileField(upload_to='pic')),
                ('des', models.TextField()),
            ],
        ),
    ]
