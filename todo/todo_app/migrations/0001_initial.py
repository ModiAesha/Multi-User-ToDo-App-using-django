# Generated by Django 5.0.6 on 2024-06-20 16:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('c', 'COMPLETED'), ('p', 'PENDING')], max_length=2)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('4', ' 4️⃣'), ('5', ' 5️⃣'), ('1', ' 1️⃣'), ('3', ' 3️⃣'), ('8', ' 8️⃣'), ('2', ' 2️⃣'), ('6', ' 6️⃣'), ('9', ' 9️⃣'), ('10', '🔟'), ('7', ' 7️⃣')], max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
