# Generated by Django 3.1.6 on 2021-02-17 11:30

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('depts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=50, verbose_name='Uuid')),
                ('name', models.CharField(max_length=200, verbose_name='Activity Name')),
                ('form_id', models.IntegerField()),
                ('form_json', django.contrib.postgres.fields.jsonb.JSONField()),
                ('document', models.FileField(upload_to='')),
                ('doc_conf', django.contrib.postgres.fields.jsonb.JSONField()),
                ('schedule', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=50, verbose_name='Uuid')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.activity')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='depts.department')),
            ],
        ),
    ]
