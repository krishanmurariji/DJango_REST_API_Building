# Generated by Django 5.0.3 on 2024-03-23 05:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('3068f336-9790-4b27-880d-90db7bd524f0'), editable=False, primary_key=True, serialize=False),
        ),
    ]
