# Generated by Django 3.2.5 on 2021-07-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment_method',
            field=models.CharField(choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('UPI', 'UPI'), ('E-Wallet', 'E-Wallet'), ('Net Banking', 'Net Banking'), ('Cash on Delivery', 'Cash on Delivery')], max_length=50),
        ),
    ]
