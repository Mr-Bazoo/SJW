# Generated by Django 5.1.3 on 2024-11-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schrijfjewijzer_app', '0007_remove_blok_signalering_kinderen_blok_kind_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blok',
            name='leerdoel',
        ),
        migrations.AddField(
            model_name='blok',
            name='leerdoel_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blok',
            name='leerdoel_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blok',
            name='leerdoel_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blok',
            name='leerdoel_4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='blok',
            name='leerdoel_5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
