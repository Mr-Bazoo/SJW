# Generated by Django 5.1.3 on 2024-11-17 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schrijfjewijzer_app', '0009_kind_remove_blok_kind_1_remove_blok_kind_2_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kind',
            options={'verbose_name_plural': 'Kinderen'},
        ),
        migrations.AlterModelOptions(
            name='leerdoel',
            options={'verbose_name_plural': 'Leerdoelen'},
        ),
        migrations.AddField(
            model_name='blok',
            name='bloknummer',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blok',
            name='lessen',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='blok',
            name='week',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
