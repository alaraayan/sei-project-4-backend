# Generated by Django 3.2.4 on 2021-06-15 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0007_auto_20210615_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sprintgoal',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Energy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy_name', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('sprint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='energies', to='sprints.sprint')),
            ],
        ),
    ]
