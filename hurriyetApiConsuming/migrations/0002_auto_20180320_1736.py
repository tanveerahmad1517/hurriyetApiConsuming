# Generated by Django 2.0.3 on 2018-03-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hurriyetApiConsuming', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_Id', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('url', models.CharField(max_length=400)),
                ('img', models.CharField(max_length=600)),
                ('tittle', models.CharField(max_length=600)),
            ],
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='Path',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]