# Generated by Django 2.0 on 2018-04-01 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableMetaData',
            fields=[
                ('which_table', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
