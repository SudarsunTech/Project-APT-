# Generated by Django 3.2.7 on 2021-12-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics_tracker_app', '0017_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('expected_percent', models.FloatField(default=0)),
                ('scored_percent', models.FloatField(default=0)),
                ('difference', models.FloatField(default=0)),
                ('outcome', models.CharField(max_length=255)),
            ],
        ),
    ]