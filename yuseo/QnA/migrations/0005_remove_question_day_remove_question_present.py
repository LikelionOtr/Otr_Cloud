# Generated by Django 4.1 on 2022-08-15 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0004_alter_answer_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='day',
        ),
        migrations.RemoveField(
            model_name='question',
            name='present',
        ),
    ]