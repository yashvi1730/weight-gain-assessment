# Generated by Django 2.2.2 on 2020-07-22 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200722_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(error_messages={'@': 'Please include a valid email address'}, max_length=254),
        ),
    ]
