# Generated by Django 4.1 on 2022-08-15 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelComp', '0012_remove_file_description_remove_file_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='file',
            name='tags',
        ),
        migrations.AddField(
            model_name='file',
            name='media',
            field=models.FileField(null=True, upload_to='ExcelComp/singlefiles'),
        ),
    ]
