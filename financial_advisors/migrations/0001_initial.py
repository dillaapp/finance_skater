# Generated by Django 4.1.5 on 2023-01-29 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinAdvisors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fin_advisor_name', models.CharField(max_length=200)),
                ('fin_advisor_username', models.CharField(max_length=200)),
                ('bio_statement', models.TextField(max_length=280)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_time', models.CharField(max_length=200)),
                ('book', models.IntegerField(default=0)),
                ('fin_advisor_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_advisors.finadvisors')),
            ],
        ),
    ]