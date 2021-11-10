# Generated by Django 3.2.9 on 2021-11-10 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_color_spare'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='priceDev_raya',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='device',
            name='imageDev',
            field=models.ImageField(blank=True, upload_to='Devices/Devices_img/', verbose_name='Image Device'),
        ),
        migrations.AlterField(
            model_name='device',
            name='img_dev_full_1',
            field=models.ImageField(blank=True, upload_to='Devices/Devices_full_img/', verbose_name='Full Image 1 (or front)'),
        ),
        migrations.AlterField(
            model_name='device',
            name='img_dev_full_2',
            field=models.ImageField(blank=True, upload_to='Devices/Devices_full_img/', verbose_name='Full Image 2 (or back)'),
        ),
        migrations.AlterField(
            model_name='spare',
            name='category',
            field=models.CharField(blank=True, choices=[('CompScreen', 'CompScreen'), ('Lcd', 'Lcd'), ('Touch', 'Touch'), ('SubBoard', 'SubBoard'), ('ChargingSocket', 'ChargingSocket'), ('HandfreeSocket', 'HandfreeSocket'), ('Board', 'Board'), ('Battery', 'Battery'), ('BackCamera', 'BackCamera'), ('FCam', 'SelfieCamera'), ('BCover', 'BackGlassCover'), ('Housing', 'Housing')], max_length=50, null=True),
        ),
    ]
