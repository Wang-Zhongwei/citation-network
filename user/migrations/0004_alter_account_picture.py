# Generated by Django 4.2.2 on 2023-07-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_account_affiliation_account_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
