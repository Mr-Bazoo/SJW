# Generated by Django 5.1.3 on 2024-11-19 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schrijfjewijzer_app', '0015_leerdoel_signalering_groep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leerdoel',
            name='doel',
            field=models.CharField(max_length=150),
        ),
    ]