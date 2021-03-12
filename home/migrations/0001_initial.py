# Generated by Django 3.0.7 on 2020-09-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tille', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contect',
            fields=[
                ('slno', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=25)),
                ('Lname', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('mob', models.IntegerField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('slno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('time_upload', models.DateTimeField(blank=True)),
                ('author', models.CharField(max_length=25)),
                ('slug', models.CharField(default='', max_length=130)),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
                ('publish', models.BooleanField()),
                ('categories', models.ManyToManyField(to='home.Categorie')),
            ],
            options={
                'ordering': ['-time_upload'],
            },
        ),
    ]