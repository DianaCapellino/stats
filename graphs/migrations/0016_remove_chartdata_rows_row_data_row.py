# Generated by Django 4.2.1 on 2023-06-01 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0015_remove_data_row_chartdata_rows_delete_row'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chartdata',
            name='rows',
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ChartData', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rows', to='graphs.chartdata')),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='row',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='row_data', to='graphs.row'),
            preserve_default=False,
        ),
    ]
