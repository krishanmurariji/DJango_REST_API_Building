# Generated by Django 5.0.3 on 2024-03-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_group_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=200)),
                ('cspeed', models.IntegerField()),
            ],
        ),
    ]
