# Generated by Django 4.2 on 2023-04-25 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_element_news_delete_newselement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='element', to='home.news'),
        ),
    ]
