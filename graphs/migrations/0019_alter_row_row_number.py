# Generated by Django 4.2.1 on 2023-06-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0018_row_row_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='row',
            name='row_number',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
