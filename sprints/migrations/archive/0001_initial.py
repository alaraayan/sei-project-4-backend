# Generated by Django 3.2.4 on 2021-06-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SprintGoals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('goal_description', models.CharField(max_length=250)),
            ],
        ),
    ]
