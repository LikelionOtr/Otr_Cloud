# Generated by Django 4.1 on 2022-08-17 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuseotext', '0002_yuseotext_time_alter_yuseotext_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yuseotext',
            name='time',
            field=models.TimeField(),
        ),
    ]