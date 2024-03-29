# Generated by Django 4.2.1 on 2023-05-30 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0003_rename_label_data_label1_chartdata_columnname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='csvFiles')),
                ('uploaded_time', models.DateTimeField(auto_now_add=True)),
                ('acitvated', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='chartdata',
            old_name='columnName',
            new_name='column_name',
        ),
        migrations.RemoveField(
            model_name='chartdata',
            name='csvFile',
        ),
        migrations.AlterField(
            model_name='chartdata',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
