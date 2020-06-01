# Generated by Django 3.0.5 on 2020-06-01 00:35

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(max_length=255)),
                ('line_1', models.CharField(blank=True, max_length=255, null=True)),
                ('line_2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', localflavor.us.models.USStateField(blank=True, max_length=2, null=True)),
                ('zip_code', localflavor.us.models.USZipCodeField(blank=True, max_length=10, null=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='contacts.Contact')),
            ],
        ),
    ]
