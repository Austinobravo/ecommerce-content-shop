# Generated by Django 4.1.2 on 2022-10-12 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_rename_image_product_first_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
