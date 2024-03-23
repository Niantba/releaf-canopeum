# Generated by Django 5.0.3 on 2024-03-23 02:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canopeum_backend', '0003_post_share_count_site_visitor_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internationalization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en', models.TextField(blank=True, db_column='EN', null=True)),
                ('fr', models.TextField(blank=True, db_column='FR', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BatchSeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canopeum_backend.batch')),
                ('tree_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canopeum_backend.treetype')),
            ],
        ),
        migrations.CreateModel(
            name='BatchSpecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canopeum_backend.batch')),
                ('tree_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canopeum_backend.treetype')),
            ],
        ),
        migrations.CreateModel(
            name='BatchSupportedSpecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canopeum_backend.batch')),
                ('tree_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='canopeum_backend.treetype')),
            ],
        ),
        migrations.DeleteModel(
            name='Batchtreetype',
        ),
    ]