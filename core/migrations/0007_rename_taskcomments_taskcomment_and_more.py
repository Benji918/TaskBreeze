# Generated by Django 5.0 on 2024-01-15 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_taskcomments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TaskComments',
            new_name='TaskComment',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='username'),
        ),
    ]
