# Generated by Django 3.1.4 on 2021-01-01 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dea', '0002_auto_20201231_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledgertransaction',
            name='ledger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credittxs', to='dea.ledger'),
        ),
        migrations.AlterField(
            model_name='ledgertransaction',
            name='ledgerno_dr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debittxns', to='dea.ledger'),
        ),
    ]
