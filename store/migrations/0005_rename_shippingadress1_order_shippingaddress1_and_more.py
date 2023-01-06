# Generated by Django 4.1.4 on 2023-01-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='shippingAdress1',
            new_name='shippingAddress1',
        ),
        migrations.AddField(
            model_name='order',
            name='billingCountry',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]