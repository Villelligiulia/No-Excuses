# Generated by Django 3.2.19 on 2023-05-25 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complete',
            new_name='done',
        ),
    ]
