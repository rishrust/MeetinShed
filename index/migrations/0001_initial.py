# Generated by Django 4.1.1 on 2022-09-25 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='meetings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('participant_id', models.CharField(max_length=1000)),
                ('time_slot', models.DateTimeField()),
                ('start_url', models.CharField(max_length=1000)),
                ('join_url', models.CharField(max_length=1000)),
                ('is_accepted', models.BooleanField(default=False)),
            ],
        ),
    ]