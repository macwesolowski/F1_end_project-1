# Generated by Django 4.2.1 on 2023-06-01 16:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=30)),
                ('pseudonym', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('excerpt', models.CharField(max_length=250)),
                ('image', models.ImageField(null=True, upload_to='posts')),
                ('date', models.DateField(auto_now=True)),
                ('txt', models.TextField(validators=[django.core.validators.MinLengthValidator(200), django.core.validators.MaxLengthValidator(3000)])),
                ('slug', models.SlugField(unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.author')),
                ('tags', models.ManyToManyField(to='blog.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_email', models.EmailField(max_length=254)),
                ('txt', models.TextField(max_length=500)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
        ),
    ]