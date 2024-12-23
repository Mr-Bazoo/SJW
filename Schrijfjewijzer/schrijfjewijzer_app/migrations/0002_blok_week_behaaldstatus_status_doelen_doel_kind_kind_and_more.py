# Generated by Django 5.1.3 on 2024-11-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schrijfjewijzer_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blok_week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blok', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='behaaldstatus',
            name='status',
            field=models.ManyToManyField(to='schrijfjewijzer_app.blok_week'),
        ),
        migrations.AddField(
            model_name='doelen',
            name='doel',
            field=models.ManyToManyField(to='schrijfjewijzer_app.blok_week'),
        ),
        migrations.AddField(
            model_name='kind',
            name='kind',
            field=models.ManyToManyField(to='schrijfjewijzer_app.blok_week'),
        ),
        migrations.AddField(
            model_name='lessen',
            name='lessen',
            field=models.ManyToManyField(to='schrijfjewijzer_app.blok_week'),
        ),
        migrations.AddField(
            model_name='momentvanvereistebeheersing',
            name='moment_beheersing',
            field=models.ManyToManyField(to='schrijfjewijzer_app.blok_week'),
        ),
        migrations.AddField(
            model_name='opmerkingen',
            name='opmerkingen',
            field=models.ManyToManyField(to='schrijfjewijzer_app.blok_week'),
        ),
        migrations.AddField(
            model_name='signaleringgroep',
            name='signaleringgroep',
            field=models.ManyToManyField(to='schrijfjewijzer_app.blok_week'),
        ),
        migrations.AddField(
            model_name='voorkennis',
            name='kennis',
            field=models.ManyToManyField(to='schrijfjewijzer_app.blok_week'),
        ),
    ]
