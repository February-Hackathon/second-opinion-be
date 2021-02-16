# Generated by Django 3.1.6 on 2021-02-11 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docs', models.FileField(upload_to='files')),
                ('owner', models.ForeignKey(default='owner doc', on_delete=django.db.models.deletion.CASCADE, related_name='owner_docs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
