# Generated by Django 4.1.4 on 2022-12-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='confess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confession', models.TextField(verbose_name='Confession')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
