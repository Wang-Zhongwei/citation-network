# Generated by Django 4.2.2 on 2023-07-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_account_affiliation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='affiliation',
        ),
        migrations.AddField(
            model_name='account',
            name='field',
            field=models.CharField(default='default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='picture',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d/'),
        ),
    ]
