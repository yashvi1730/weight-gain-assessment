# Generated by Django 2.2.2 on 2020-07-22 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(error_messages={'invalid': 'Please include a valid email address'}, max_length=254),
        ),
    ]