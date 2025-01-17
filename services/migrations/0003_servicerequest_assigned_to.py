# Generated by Django 5.1.3 on 2024-11-15 08:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_servicerequest_fileattachment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='assigned_to',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_staff': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
