# Generated by Django 5.1.5 on 2025-01-20 15:29

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='название')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='название')),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish', verbose_name='URL')),
                ('body', models.TextField(verbose_name='контент')),
                ('image_prevu', models.ImageField(blank=True, upload_to='photos/prevu/%Y/%m/%d/', verbose_name='Фото для превью')),
                ('image_post', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото для поста')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='опубликовано')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='обновлено')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10, verbose_name='статус')),
                ('author', models.ForeignKey(default='admin', on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.postcategory', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
