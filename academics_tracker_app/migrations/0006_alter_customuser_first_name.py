# Generated by Django 3.2.7 on 2021-11-16 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics_tracker_app', '0005_studentresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
