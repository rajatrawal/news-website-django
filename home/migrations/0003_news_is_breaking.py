# Generated by Django 4.2 on 2023-04-24 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_newsthumbnill'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_breaking',
            field=models.BooleanField(default=False),
        ),
    ]
