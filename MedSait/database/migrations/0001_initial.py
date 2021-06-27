# Generated by Django 3.2 on 2021-05-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('sex', models.CharField(max_length=100, verbose_name='Пол пациента')),
                ('insurance', models.CharField(max_length=100, verbose_name='Страховая организация')),
                ('policy', models.CharField(max_length=100, verbose_name='Страховое свидетельство')),
                ('address', models.CharField(max_length=100, verbose_name='Домашний адрес')),
                ('number_phone', models.CharField(max_length=100, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=100, verbose_name='Электронная почта')),
                ('parent_name', models.CharField(max_length=100, verbose_name='ФИО родителя')),
                ('parent_number_phone', models.CharField(max_length=100, verbose_name='Номер телефона родителя')),
                ('parent_email', models.EmailField(max_length=100, verbose_name='Электронная почта родителя')),
                ('nation', models.CharField(max_length=100, verbose_name='Нация пациента')),
                ('mother_nation', models.CharField(max_length=100, verbose_name='Нация матери пациента')),
                ('father_nation', models.CharField(max_length=100, verbose_name='Нация отца пациента')),
                ('registration_date', models.DateField(verbose_name='Дата регистрации пациента')),
            ],
            options={
                'verbose_name': 'Пациент',
                'verbose_name_plural': 'Пациенты',
            },
        ),
    ]