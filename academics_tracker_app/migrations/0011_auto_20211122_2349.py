# Generated by Django 3.2.7 on 2021-11-22 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics_tracker_app', '0010_auto_20211122_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentresult',
            name='student_id',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (2, 'exam')], default=1, max_length=10),
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]
