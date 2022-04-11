# Generated by Django 3.2.7 on 2021-11-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics_tracker_app', '0008_auto_20211118_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancereport',
            name='attendance_id',
        ),
        migrations.RemoveField(
            model_name='attendancereport',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='feedbackexams',
            name='exam_id',
        ),
        migrations.RemoveField(
            model_name='feedbackstudent',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='leavereportexam',
            name='exam_id',
        ),
        migrations.RemoveField(
            model_name='leavereportstudent',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='notificationexams',
            name='examf_id',
        ),
        migrations.RemoveField(
            model_name='notificationstudent',
            name='student_id',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='AttendanceReport',
        ),
        migrations.DeleteModel(
            name='FeedBackexams',
        ),
        migrations.DeleteModel(
            name='FeedBackStudent',
        ),
        migrations.DeleteModel(
            name='LeaveReportexam',
        ),
        migrations.DeleteModel(
            name='LeaveReportStudent',
        ),
        migrations.DeleteModel(
            name='Notificationexams',
        ),
        migrations.DeleteModel(
            name='NotificationStudent',
        ),
    ]