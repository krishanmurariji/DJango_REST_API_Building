# Generated by Django 5.0.3 on 2024-03-23 11:00

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_contact_alter_todo_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('add', models.CharField(max_length=100)),
                ('dis', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('f9b4cb6f-c3fe-41c8-b42b-11bbfb85342d'), editable=False, primary_key=True, serialize=False),
        ),
    ]