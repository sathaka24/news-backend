# Generated by Django 2.1 on 2024-11-07 00:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialJournalism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
