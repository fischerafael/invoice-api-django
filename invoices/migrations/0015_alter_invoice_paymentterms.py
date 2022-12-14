# Generated by Django 4.1 on 2022-09-14 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0014_invoice_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='paymentTerms',
            field=models.CharField(choices=[('eob', 'end of business day'), ('eom', 'end of month')], default='eom', max_length=62),
        ),
    ]
