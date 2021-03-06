# Generated by Django 2.0 on 2018-04-11 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_auto_20180406_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('subrace_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subraces', to='people.Race')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='population',
            name='sub_population_of',
        ),
        migrations.RemoveField(
            model_name='god',
            name='follower_populations',
        ),
        migrations.RemoveField(
            model_name='person',
            name='populations_in',
        ),
        migrations.AlterField(
            model_name='person',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members_of_race', to='people.Race'),
        ),
        migrations.DeleteModel(
            name='Population',
        ),
        migrations.AddField(
            model_name='god',
            name='follower_races',
            field=models.ManyToManyField(blank=True, related_name='gods_followed', to='people.Race'),
        ),
    ]
