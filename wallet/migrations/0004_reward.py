# Generated by Django 4.0.6 on 2022-08-01 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_delete_reward'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(max_length=1)),
                ('Name', models.CharField(max_length=15)),
            ],
        ),
    ]