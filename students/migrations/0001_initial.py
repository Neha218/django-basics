# Generated by Django 4.0 on 2021-12-28 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField()),
                ('photo', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('full_name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=100)),
            ],
        ),
    ]
