# Generated by Django 3.2.12 on 2022-03-28 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_remove_feed_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_id', models.IntegerField(default=0)),
                ('email', models.EmailField(default='', max_length=254)),
                ('is_markerd', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_id', models.IntegerField(default=0)),
                ('email', models.EmailField(default='', max_length=254)),
                ('is_like', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_id', models.IntegerField(default=0)),
                ('email', models.EmailField(default='', max_length=254)),
                ('reply_content', models.TextField()),
            ],
        ),
    ]