# Generated by Django 4.0.2 on 2022-03-29 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('image_names', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]