# Generated by Django 3.2.7 on 2021-09-28 10:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0003_auto_20210928_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]