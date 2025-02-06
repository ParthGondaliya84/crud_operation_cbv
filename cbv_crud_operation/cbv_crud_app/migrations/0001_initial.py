# Generated by Django 5.1.5 on 2025-02-06 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=70)),
                ('leader_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('total_employee', models.IntegerField()),
            ],
        ),
    ]
