# Generated by Django 4.1.1 on 2022-09-15 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0015_alter_invoice_paymentterms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='services',
        ),
        migrations.CreateModel(
            name='InvoiceServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='services', to='invoices.invoice')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoices', to='invoices.service')),
            ],
        ),
    ]
