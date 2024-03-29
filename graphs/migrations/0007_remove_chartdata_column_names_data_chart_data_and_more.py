# Generated by Django 4.2.1 on 2023-05-30 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0006_column_alter_chartdata_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chartdata',
            name='column_names',
        ),
        migrations.AddField(
            model_name='data',
            name='chart_data',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='chart_datas', to='graphs.chartdata'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Column',
        ),
    ]
