# Generated by Django 3.2.9 on 2021-11-15 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0003_alter_brand_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='spare',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='spare',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mobile.brand'),
        ),
        migrations.AlterField(
            model_name='spare',
            name='device_main',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Device_sets', to='mobile.device'),
        ),
        migrations.AlterField(
            model_name='spare',
            name='new_or_not',
            field=models.BooleanField(default=True, verbose_name='New'),
        ),
        migrations.AlterField(
            model_name='spare',
            name='warranty',
            field=models.IntegerField(default=1, verbose_name='Warranty'),
        ),
    ]
