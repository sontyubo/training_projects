# Generated by Django 4.2.7 on 2023-11-25 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopTip', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoptipmodel',
            name='delete_date',
        ),
        migrations.AlterField(
            model_name='shoptipmodel',
            name='register_date',
            field=models.DateField(auto_now=True),
        ),
    ]
