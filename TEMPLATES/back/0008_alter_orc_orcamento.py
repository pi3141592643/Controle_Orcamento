# Generated by Django 4.0.5 on 2022-06-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitaorcamento', '0007_orc_orcamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orc',
            name='orcamento',
            field=models.CharField(blank=True, default='0,00', max_length=15, null=True),
        ),
    ]
