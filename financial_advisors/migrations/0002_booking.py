# Generated by Django 4.1.5 on 2023-02-02 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financial_advisors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=150)),
                ('email', models.TextField(max_length=150)),
                ('day_and_time', models.TextField(max_length=150)),
                ('location', models.TextField(max_length=280)),
                ('topic', models.TextField(max_length=280)),
                ('fin_advisor_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_advisors.finadvisors')),
            ],
        ),
    ]
