# Generated by Django 4.1.4 on 2022-12-28 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_usertype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='addeess',
            new_name='address',
        ),
    ]
