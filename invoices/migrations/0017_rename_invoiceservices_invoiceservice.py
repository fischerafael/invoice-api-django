# Generated by Django 4.1.1 on 2022-09-15 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0016_remove_invoice_services_invoiceservices'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvoiceServices',
            new_name='InvoiceService',
        ),
    ]
