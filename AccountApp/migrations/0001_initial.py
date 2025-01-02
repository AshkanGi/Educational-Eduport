# Generated by Django 5.1.4 on 2025-01-02 11:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'رمز یکبار مصرف',
                'verbose_name_plural': 'رمز های یکبار مصرف',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='ایمیل')),
                ('full_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='نام کامل')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='شماره موبایل')),
                ('bio', models.TextField(max_length=225, verbose_name='راجب من')),
                ('image', models.ImageField(blank=True, upload_to='profile/user', verbose_name='عکس')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ عضویت')),
                ('last_login', models.DateTimeField(auto_now=True, null=True, verbose_name='اخرین ورود')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_admin', models.BooleanField(default=False, verbose_name='ادمین')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
    ]
