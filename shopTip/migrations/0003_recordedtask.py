# Generated by Django 4.2.7 on 2023-11-28 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopTip', '0002_remove_shoptipmodel_delete_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordedTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('memo', models.TextField()),
                ('register_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
