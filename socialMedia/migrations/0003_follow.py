# Generated by Django 4.2.5 on 2024-06-13 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialMedia', '0002_postreaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('follower', 'following')},
            },
        ),
    ]
