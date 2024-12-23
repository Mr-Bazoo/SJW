# Generated by Django 5.1.3 on 2024-11-19 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schrijfjewijzer_app', '0012_kind_keuze1_kind_keuze2_kind_keuze3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kind',
            name='keuze1',
        ),
        migrations.RemoveField(
            model_name='kind',
            name='keuze2',
        ),
        migrations.RemoveField(
            model_name='kind',
            name='keuze3',
        ),
        migrations.RemoveField(
            model_name='leerdoel',
            name='automatiseringsdoelen',
        ),
        migrations.RemoveField(
            model_name='leerdoel',
            name='kinderen',
        ),
        migrations.RemoveField(
            model_name='leerdoel',
            name='lessen',
        ),
        migrations.RemoveField(
            model_name='leerdoel',
            name='opmerkingen',
        ),
        migrations.RemoveField(
            model_name='leerdoel',
            name='sleepdoel',
        ),
        migrations.RemoveField(
            model_name='leerdoel',
            name='voorkennis',
        ),
        migrations.CreateModel(
            name='LeerdoelScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keuze1', models.IntegerField(choices=[(2, 'x'), (1, '~'), (0, 'v')], default=0)),
                ('keuze2', models.IntegerField(choices=[(2, 'x'), (1, '~'), (0, 'v')], default=0)),
                ('keuze3', models.IntegerField(choices=[(2, 'x'), (1, '~'), (0, 'v')], default=0)),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='schrijfjewijzer_app.kind')),
                ('leerdoel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='schrijfjewijzer_app.leerdoel')),
            ],
            options={
                'verbose_name_plural': 'Leerdoel Scores',
                'unique_together': {('kind', 'leerdoel')},
            },
        ),
    ]
