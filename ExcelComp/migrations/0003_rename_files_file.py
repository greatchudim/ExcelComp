# Generated by Django 4.1 on 2022-08-11 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelComp', '0002_files_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Files',
            new_name='File',
        ),
    ]