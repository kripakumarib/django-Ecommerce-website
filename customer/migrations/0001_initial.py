# Generated by Django 4.1.7 on 2023-03-22 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_brandname_products_review_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyproducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('image', models.ImageField(upload_to='uploads/products/')),
                ('Products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_product', to='account.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]