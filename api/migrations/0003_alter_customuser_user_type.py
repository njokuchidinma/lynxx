# Generated by Django 4.2.5 on 2023-09-14 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_customuser_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('admin', 'ADMIN'), ('staff', 'STAFF'), ('customer', 'CUSTOMER')], default='customer', max_length=10),
        ),
    ]
