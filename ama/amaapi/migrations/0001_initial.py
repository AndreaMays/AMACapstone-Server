# Generated by Django 3.2.4 on 2021-06-10 19:13

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
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('studio_name', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name_of_comp', models.CharField(max_length=50)),
                ('type_of_award', models.CharField(max_length=50)),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='amaapi.admin')),
            ],
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_first_name', models.CharField(max_length=50)),
                ('parent_last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('birth_date', models.CharField(max_length=50)),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='amaapi.admin')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LessonNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('scale_notes', models.TextField(max_length=255)),
                ('memory_notes', models.TextField(max_length=255)),
                ('song1_notes', models.TextField(max_length=255)),
                ('song2_notes', models.TextField(max_length=255)),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='amaapi.admin')),
                ('student_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amaapi.studentuser')),
            ],
        ),
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name_of_comp', models.CharField(max_length=50)),
                ('score', models.CharField(max_length=50)),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='amaapi.admin')),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amaapi.awards')),
                ('student_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amaapi.studentuser')),
            ],
        ),
        migrations.AddField(
            model_name='awards',
            name='student_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amaapi.studentuser'),
        ),
    ]