# Generated by Django 3.1 on 2021-05-04 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0008_auto_20210430_0447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Наименование')),
                ('director', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='own_organization', to=settings.AUTH_USER_MODEL, verbose_name='director')),
                ('employee', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='employee')),
            ],
        ),
    ]
