# Generated by Django 4.2.11 on 2024-04-30 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_cartitem_amount_cartitem_discount_order_promo_promo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='name',
            field=models.CharField(max_length=8),
        ),
    ]
