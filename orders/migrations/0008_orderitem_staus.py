# Generated by Django 3.2.3 on 2021-05-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_orderitem_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='staus',
            field=models.CharField(choices=[('c', 'In Cart'), ('o', 'Ordered')], default='c', max_length=1),
        ),
    ]
