# Generated by Django 2.1 on 2024-10-30 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genaral_news', '0003_alter_news_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialJournalism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
