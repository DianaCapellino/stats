# Generated by Django 4.2.1 on 2023-05-29 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0002_chart_data_charttemplate_chartdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='label',
            new_name='label1',
        ),
        migrations.AddField(
            model_name='chartdata',
            name='columnName',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='label2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
