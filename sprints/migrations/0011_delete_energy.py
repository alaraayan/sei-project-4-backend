# Generated by Django 3.2.4 on 2021-06-15 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0010_remove_energy_energy_level'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Energy',
        ),
    ]
