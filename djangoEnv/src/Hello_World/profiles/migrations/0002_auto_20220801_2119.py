# Generated by Django 2.1.5 on 2022-08-01 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prefix', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], max_length=5)),
                ('FirstName', models.CharField(max_length=60)),
                ('LastName', models.CharField(max_length=60)),
                ('Email', models.CharField(max_length=60)),
                ('Username', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
