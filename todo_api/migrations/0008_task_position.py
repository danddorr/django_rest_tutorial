# Generated by Django 5.0.6 on 2024-06-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0007_usertasklist_position_delete_itemposition'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]