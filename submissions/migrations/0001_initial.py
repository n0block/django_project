# Generated by Django 3.0.7 on 2020-06-22 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=100)),
                ('vendor_name', models.CharField(max_length=100)),
                ('description_text', models.TextField()),
                ('submission_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('classification', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='submissions.Classification')),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]