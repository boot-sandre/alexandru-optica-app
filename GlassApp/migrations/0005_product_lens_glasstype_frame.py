# Generated by Django 4.2.7 on 2023-11-07 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GlassApp', '0004_alter_contact_order_alter_identity_order_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Lens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='GlassApp.product')),
            ],
        ),
        migrations.CreateModel(
            name='GlassType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.CharField(max_length=100)),
                ('near', models.CharField(max_length=100)),
                ('other', models.CharField(max_length=100)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='GlassApp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='GlassApp.product')),
            ],
        ),
    ]