# Generated by Django 3.1.5 on 2021-03-04 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourapp', '0002_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('indoor', 'indoor'), ('outdoor', 'outdoor')], max_length=200, null=True),
        ),
    ]
