# Generated by Django 4.2.7 on 2023-11-19 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("optica_app", "0002_voucher_voucherline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="voucherline",
            name="voucher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="voucher_lines",
                to="optica_app.voucher",
            ),
        ),
    ]