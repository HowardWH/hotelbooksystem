# Generated by Django 2.0.5 on 2018-06-02 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("backend", "0004_hotel_order_backgroud")]

    operations = [
        migrations.RenameField(
            model_name="hotel",
            old_name="order_backgroud",
            new_name="order_background",
        )
    ]
