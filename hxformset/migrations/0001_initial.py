# Generated by Django 5.1.6 on 2025-02-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1024)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('done', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
