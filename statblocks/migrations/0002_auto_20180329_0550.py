# Generated by Django 2.0 on 2018-03-29 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statblocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monster',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='monster',
            name='name',
            field=models.CharField(default='name', max_length=255),
            preserve_default=False,
        ),
    ]
