# Generated by Django 4.2.1 on 2023-05-12 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('head_app', '0003_musician_alter_performing_options_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='musicians',
            field=models.ManyToManyField(to='head_app.musician'),
        ),
        migrations.AddField(
            model_name='guitar',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
