# Generated by Django 5.1.3 on 2024-11-16 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schrijfjewijzer_app', '0004_alter_behaaldstatus_status_blok_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='behaaldstatus',
            options={'verbose_name_plural': 'Behaaldstatus'},
        ),
        migrations.AlterModelOptions(
            name='blok_week',
            options={'verbose_name_plural': 'Blok_week'},
        ),
        migrations.AlterModelOptions(
            name='doelen',
            options={'verbose_name_plural': 'Doelen'},
        ),
        migrations.AlterModelOptions(
            name='kind',
            options={'verbose_name_plural': 'Kind'},
        ),
        migrations.AlterModelOptions(
            name='lessen',
            options={'verbose_name_plural': 'Lessen'},
        ),
        migrations.AlterModelOptions(
            name='momentvanvereistebeheersing',
            options={'verbose_name_plural': 'MomentVanVereisteBeheersing'},
        ),
        migrations.AlterModelOptions(
            name='myinteger',
            options={'verbose_name_plural': 'MyInteger'},
        ),
        migrations.AlterModelOptions(
            name='opmerkingen',
            options={'verbose_name_plural': 'Opmerkingen'},
        ),
        migrations.AlterModelOptions(
            name='signaleringgroep',
            options={'verbose_name_plural': 'SignaleringGroep'},
        ),
        migrations.AlterModelOptions(
            name='voorkennis',
            options={'verbose_name_plural': 'Voorkennis'},
        ),
    ]