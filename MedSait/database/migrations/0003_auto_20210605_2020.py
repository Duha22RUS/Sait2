# Generated by Django 3.2 on 2021-06-05 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20210519_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='abundant_periods2',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Нет'), (2, 'Да')], default=1, verbose_name='Обильные месячные'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='articles_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='database.articles'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='bleeding_gums2',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Нет'), (2, 'Да')], default=1, verbose_name='Кровоточивость дёсен'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='bruising2',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Нет'), (2, 'Да')], default=1, verbose_name='Синячковость'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='father_infarct',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Нет'), (2, 'Да'), (3, 'Не знаю')], default=1, verbose_name='Был ли у отца инфаркт, инсульт, тромбоз до 55 лет'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='grand_infarct',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Нет'), (2, 'Да'), (3, 'Не знаю')], default=1, verbose_name='Был ли у деда/бабушки инфаркт, инсульт, тромбоз, до 65 лет'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='heart_surgery',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Нет'), (2, 'Да'), (3, 'Не знаю')], default=1, verbose_name='Операции на сердце и сосудах'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='mother_infarct',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Нет'), (2, 'Да'), (3, 'Не знаю')], default=1, verbose_name='Был ли у матери инфаркт, инсульт, тромбоз до 65 лет'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='myocardial_infarction',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Нет'), (2, 'Да'), (3, 'Не знаю')], default=1, verbose_name='Инфаркт миокарда'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='nosebleeds2',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Справа'), (2, 'Слева'), (3, 'Справа и слева'), (4, 'Нет')], default=1, verbose_name='Носовые кровотечения'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='other_bleeding2',
            field=models.CharField(default=1, max_length=100, verbose_name='Другая кровоточивость'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complaints',
            name='stroke',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Нет'), (2, 'Да'), (3, 'Не знаю')], default=1, verbose_name='Инсульт (ТИА, ОНМК)'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='thrombosis',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Нет'), (2, 'Да'), (3, 'Не знаю')], default=1, verbose_name='Тромбозы'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='father_nation',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Русские'), (2, 'Украинцы'), (3, 'Немцы'), (4, 'Казахи'), (5, 'Белорусы'), (6, 'Алтайцы'), (7, 'Кумандинцы'), (8, 'Татары'), (9, 'ДРУГАЯ')], default=1, verbose_name='Нация отца пациента'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='mother_nation',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Русские'), (2, 'Украинцы'), (3, 'Немцы'), (4, 'Казахи'), (5, 'Белорусы'), (6, 'Алтайцы'), (7, 'Кумандинцы'), (8, 'Татары'), (9, 'ДРУГАЯ')], default=1, verbose_name='Нация матери пациента'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='nation',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Русские'), (2, 'Украинцы'), (3, 'Немцы'), (4, 'Казахи'), (5, 'Белорусы'), (6, 'Алтайцы'), (7, 'Кумандинцы'), (8, 'Татары'), (9, 'ДРУГАЯ')], default=1, verbose_name='Нация пациента'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='sex',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Мужской'), (2, 'Женский')], default=1, verbose_name='Пол пациента'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Пациент')], default=1, verbose_name='Название'),
        ),
    ]
