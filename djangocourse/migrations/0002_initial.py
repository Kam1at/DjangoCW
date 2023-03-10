# Generated by Django 4.1.6 on 2023-03-04 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('djangocourse', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='distributionlist',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangocourse.client'),
        ),
        migrations.AddField(
            model_name='distributionlist',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangocourse.message'),
        ),
        migrations.AddField(
            model_name='distributionlist',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='client',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
