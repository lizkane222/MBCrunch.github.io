# Generated by Django 3.1.2 on 2020-10-06 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('WA', 'waste'), ('CA', 'cardboard'), ('EW', 'e-waste'), ('GL', 'glass'), ('ME', 'metal'), ('PA', 'paper'), ('PL', 'plastic'), ('OR', 'organic')], default='WA', max_length=2)),
                ('location', models.CharField(max_length=200)),
                ('collection_market', models.TextField(max_length=550)),
                ('delivery_date', models.IntegerField()),
                ('delivery_location', models.CharField(max_length=200)),
                ('verified', models.BooleanField(verbose_name=False)),
                ('sponsor', models.CharField(max_length=100)),
                ('gives_rewards', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=500)),
                ('deposits_made', models.IntegerField()),
                ('community_contributions', models.IntegerField()),
                ('verifications', models.CharField(choices=[('UV', 'unverified'), ('VE', 'verified'), ('AC', 'accurate bin type'), ('IN', 'inaccurate bin type'), ('EX', 'exists'), ('NO', 'does not exist'), ('GO', 'good condition'), ('PO', 'poor condition')], default='UV', max_length=2)),
                ('current_location', models.CharField(max_length=200)),
                ('sponsor', models.CharField(max_length=200)),
                ('identify_new_bin', models.CharField(max_length=200)),
                ('gives_rewards', models.IntegerField()),
                ('bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bin')),
            ],
        ),
    ]