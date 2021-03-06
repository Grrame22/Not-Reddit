# Generated by Django 3.0.8 on 2020-07-31 13:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date of writing')),
                ('url', models.SlugField(blank=True, max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='ArticleColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=50, unique=True, verbose_name='Theme')),
            ],
            options={
                'verbose_name': 'Theme',
                'verbose_name_plural': 'Themes',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=150, unique=True, verbose_name='Gender')),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Gender',
            },
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=150, unique=True, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name='User')),
                ('facebook', models.URLField(blank=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, verbose_name='Instagram')),
                ('twitter', models.URLField(blank=True, verbose_name='Twitter')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Gender', to='startup.Gender')),
                ('preference_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Preference', to='startup.Preferences')),
            ],
            options={
                'verbose_name': 'Preference',
                'verbose_name_plural': 'Preferences',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=150, verbose_name='Description')),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
                ('articles_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startup.Article')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='startup.Preferences'),
        ),
        migrations.AddField(
            model_name='article',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Theme', to='startup.ArticleColor'),
        ),
    ]
