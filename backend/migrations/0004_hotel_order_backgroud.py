# Generated by Django 2.0.5 on 2018-06-02 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("backend", "0003_auto_20180602_2338")]

    operations = [
        migrations.AddField(
            model_name="hotel",
            name="order_backgroud",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        )
    ]
