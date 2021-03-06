# Generated by Django 2.2 on 2021-08-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_portfolio_imageorvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=12)),
                ('document', models.FileField(upload_to='documents/')),
            ],
            options={
                'verbose_name': 'Career',
                'verbose_name_plural': 'Career',
                'db_table': 'tbl_career',
                'managed': True,
            },
        ),
    ]
