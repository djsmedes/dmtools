# Generated by Django 2.0 on 2018-03-25 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MiscFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PoliticalFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WaterFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Continent',
        ),
        migrations.RemoveField(
            model_name='nation',
            name='id',
        ),
        migrations.RemoveField(
            model_name='nation',
            name='name',
        ),
        migrations.RemoveField(
            model_name='world',
            name='id',
        ),
        migrations.RemoveField(
            model_name='world',
            name='name',
        ),
        migrations.CreateModel(
            name='Lake',
            fields=[
                ('waterfeature_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='places.WaterFeature')),
            ],
            options={
                'abstract': False,
            },
            bases=('places.waterfeature',),
        ),
        migrations.CreateModel(
            name='Landmass',
            fields=[
                ('geofeature_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='places.GeoFeature')),
            ],
            options={
                'abstract': False,
            },
            bases=('places.geofeature',),
        ),
        migrations.CreateModel(
            name='Mountain',
            fields=[
                ('geofeature_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='places.GeoFeature')),
            ],
            options={
                'abstract': False,
            },
            bases=('places.geofeature',),
        ),
        migrations.CreateModel(
            name='MountainRange',
            fields=[
                ('geofeature_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='places.GeoFeature')),
            ],
            options={
                'abstract': False,
            },
            bases=('places.geofeature',),
        ),
        migrations.CreateModel(
            name='Ocean',
            fields=[
                ('waterfeature_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='places.WaterFeature')),
            ],
            options={
                'abstract': False,
            },
            bases=('places.waterfeature',),
        ),
        migrations.CreateModel(
            name='River',
            fields=[
                ('waterfeature_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='places.WaterFeature')),
                ('source', models.CharField(max_length=255)),
                ('terminus', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('places.waterfeature',),
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('politicalfeature_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='places.PoliticalFeature')),
                ('size_class', models.CharField(choices=[('ME', 'Metropolis'), ('CI', 'City'), ('TO', 'Town'), ('VI', 'Village')], max_length=2)),
            ],
            options={
                'abstract': False,
            },
            bases=('places.politicalfeature',),
        ),
        migrations.AddField(
            model_name='nation',
            name='politicalfeature_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='places.PoliticalFeature'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='world',
            name='politicalfeature_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='places.PoliticalFeature'),
            preserve_default=False,
        ),
    ]
