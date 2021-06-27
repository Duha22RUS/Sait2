from django.db import models

class Articles(models.Model):
    TITLEFIELD = [(1, 'Пациент')]
    SEX = [(1, 'Мужской'), (2, 'Женский')]
    NATION = [(1, 'Русские'), (2, 'Украинцы'), (3, 'Немцы'), (4, 'Казахи'), (5, 'Белорусы'), (6, 'Алтайцы'), (7, 'Кумандинцы'), (8, 'Татары'), (9, 'ДРУГАЯ')]

    title = models.PositiveSmallIntegerField('Название', choices=TITLEFIELD, default=1)
    name = models.CharField('ФИО', max_length=100)
    date_of_birth = models.DateField('Дата рождения')
    sex = models.PositiveSmallIntegerField('Пол пациента', choices=SEX, default=1)
    insurance = models.CharField('Страховая организация', max_length=100)
    policy = models.CharField('Страховое свидетельство', max_length=100)
    address = models.CharField('Домашний адрес', max_length=100)
    number_phone = models.CharField('Номер телефона', max_length=100)
    email = models.EmailField('Электронная почта', max_length=100)
    parent_name = models.CharField('ФИО родителя', max_length=100)
    parent_number_phone = models.CharField('Номер телефона родителя', max_length=100)
    parent_email = models.EmailField('Электронная почта родителя', max_length=100)
    nation = models.PositiveSmallIntegerField('Нация пациента', choices=NATION, default=1)
    mother_nation = models.PositiveSmallIntegerField('Нация матери пациента', choices=NATION, default=1)
    father_nation = models.PositiveSmallIntegerField('Нация отца пациента', choices=NATION, default=1)
    registration_date = models.DateField('Дата регистрации пациента')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

RIGHT = 1
LEFT = 2
RIGHTLEFT = 3
NO = 4
YES = 5
MORNING = 6
DAY = 7
NIGHT = 8
EVENING = 9
PHYSLOAD = 10
MENTALLOAD = 11
STRESS = 12
SPRING = 13
AUTUMN = 14
DONTKNOW = 15

class Complaints(models.Model):
    articles_id = models.ForeignKey('Articles', on_delete=models.CASCADE, null=True)
    name2 = models.CharField('ФИО', max_length=100, default=1)

    NOSEBLOOD = [(RIGHT, 'Справа'), (LEFT, 'Слева'), (RIGHTLEFT, 'Справа и слева'), (NO, 'Нет')]
    YESNO = [(NO, 'Нет'), (YES, 'Да')]
    PROVOKATE = [(MORNING, 'Утро'), (DAY, 'День'), (NIGHT, 'Ночь'), (EVENING, 'Вечер'), (PHYSLOAD, 'Физ нагрузка'),
                 (MENTALLOAD, 'Умственная нагрузка'), (STRESS, 'Стресс'), (SPRING, 'Весна'), (AUTUMN, 'Осень')]
    YESNODONTKNOW = [(NO, 'Нет'), (YES, 'Да'), (DONTKNOW, 'Не знаю')]

    # Жалобы
    date_receipt = models.DateField('Дата приёма', db_column='Дата приёма')
    nosebleeds = models.PositiveSmallIntegerField('Носовые кровотечения', choices=NOSEBLOOD, default=NO, db_column='Носовые кровотечения')
    nosebleeds_per_month = models.CharField('Количество носовых кровотечений в месяц', max_length=100, db_column='Количество носовых кровотечений в месяц')
    abundant_periods = models.PositiveSmallIntegerField('Обильные месячные', choices=YESNO, default=NO, db_column='Обильные месячные')
    bleeding_gums = models.PositiveSmallIntegerField('Кровоточивость дёсен', choices=YESNO, default=NO, db_column='Кровоточивость дёсен')
    bruising = models.PositiveSmallIntegerField('Синячковость', choices=YESNO, default=NO, db_column='Синячковость')
    other_bleeding = models.CharField('Другая кровоточивость', max_length=100, db_column='Другая кровоточивость')
    duration_of_bleeding = models.IntegerField('Длительность кровоточивости(мин)', db_column='Длительность кровоточивости(мин)')
    fainting = models.PositiveSmallIntegerField('Обмороки', choices=YESNO, default=NO, db_column='Обмороки')
    dizziness = models.PositiveSmallIntegerField('Головокружения', choices=YESNO, default=NO, db_column='Головокружения')
    heart_pain = models.PositiveSmallIntegerField('Боль в области сердца', choices=YESNO, default=NO, db_column='Боль в области сердца')
    others = models.CharField('Другие', max_length=100, db_column='Другие')
    first_appearance = models.IntegerField('Первое появление, возраст', db_column='Первое появление, возраст')
    provocation_of_nosebleeds = models.PositiveSmallIntegerField('Провокация носовых кровотечений', choices=PROVOKATE, default=MORNING, db_column='Провокация носовых кровотечений')

    # У родственников
    nosebleeds2 = models.PositiveSmallIntegerField('Носовые кровотечения', choices=NOSEBLOOD, default=NO)
    abundant_periods2 = models.PositiveSmallIntegerField('Обильные месячные', choices=YESNO, default=NO)
    bleeding_gums2 = models.PositiveSmallIntegerField('Кровоточивость дёсен', choices=YESNO, default=NO)
    bruising2 = models.PositiveSmallIntegerField('Синячковость', choices=YESNO, default=NO)
    other_bleeding2 = models.CharField('Другая кровоточивость', max_length=100)
    father_infarct = models.PositiveSmallIntegerField('Был ли у отца инфаркт, инсульт, тромбоз до 55 лет', choices=YESNODONTKNOW, default=NO)
    mother_infarct = models.PositiveSmallIntegerField('Был ли у матери инфаркт, инсульт, тромбоз до 65 лет', choices=YESNODONTKNOW, default=NO)
    grand_infarct = models.PositiveSmallIntegerField('Был ли у деда/бабушки инфаркт, инсульт, тромбоз, до 65 лет', choices=YESNODONTKNOW, default=NO)

    # Перенесенные заболевания | Сопутствующие заболевания | Соматические заболевания
    myocardial_infarction = models.PositiveSmallIntegerField('Инфаркт миокарда', choices=YESNODONTKNOW, default=NO)
    stroke = models.PositiveSmallIntegerField('Инсульт (ТИА, ОНМК)', choices=YESNODONTKNOW, default=NO)
    thrombosis = models.PositiveSmallIntegerField('Тромбозы', choices=YESNODONTKNOW, default=NO)
    heart_surgery = models.PositiveSmallIntegerField('Операции на сердце и сосудах', choices=YESNODONTKNOW, default=NO)

    cancer_disease = models.PositiveSmallIntegerField('Онкологическое заболевание', choices=YESNODONTKNOW, default=NO)
    hypertonic_disease = models.PositiveSmallIntegerField('Гипертоническая болезнь', choices=YESNODONTKNOW, default=NO)
    work_of_the_heart = models.PositiveSmallIntegerField('Перебои в работе сердца', choices=YESNODONTKNOW, default=NO)
    atrial_fibrillation = models.PositiveSmallIntegerField('Фибрилляция предсердий', choices=YESNODONTKNOW, default=NO)
    diabetes = models.PositiveSmallIntegerField('Сахарный диабет', choices=YESNODONTKNOW, default=NO)
    varicose_veins = models.PositiveSmallIntegerField('Варикозная болезнь', choices=YESNODONTKNOW, default=NO)
    flat_feet = models.PositiveSmallIntegerField('Плоскостопие/гипермобильность суставов', choices=YESNODONTKNOW, default=NO)
    fainting2 = models.PositiveSmallIntegerField('Обмороки', choices=YESNODONTKNOW, default=NO)
    dizziness2 = models.PositiveSmallIntegerField('Головокружения', choices=YESNODONTKNOW, default=NO)
    obesity = models.PositiveSmallIntegerField('Ожирение', choices=YESNODONTKNOW, default=NO)

    bronchial_asthma = models.PositiveSmallIntegerField('Бронхиальная астма', choices=YESNODONTKNOW, default=NO)
    ari_times_a_year = models.PositiveSmallIntegerField('ОРИ > 4 раз в год', choices=YESNODONTKNOW, default=NO)
    diseases_of_the_thyroid_gland = models.PositiveSmallIntegerField('Заболевания щитовидной железы', choices=YESNODONTKNOW, default=NO)
    chronic_pyelonephritis = models.PositiveSmallIntegerField('Хронический пиелонефрит', choices=YESNODONTKNOW, default=NO)
    chronic_gastritis = models.PositiveSmallIntegerField('Хронический гастрит', choices=YESNODONTKNOW, default=NO)
    arrhythmia = models.PositiveSmallIntegerField('Аритмия', choices=YESNODONTKNOW, default=NO)
    vegetovascular_dystonia = models.PositiveSmallIntegerField('Вегето-сосудистая дистония', choices=YESNODONTKNOW, default=NO)
    migraine = models.PositiveSmallIntegerField('Мигрени', choices=YESNODONTKNOW, default=NO)
    osteochondrosis = models.PositiveSmallIntegerField('Остеохондроз', choices=YESNODONTKNOW, default=NO)
    loss_of_visual_fields = models.PositiveSmallIntegerField('Выпадение полей зрения', choices=YESNODONTKNOW, default=NO)
    heart_defects = models.PositiveSmallIntegerField('Пороки сердца', choices=YESNODONTKNOW, default=NO)
    neuroendocrine_syndrome = models.PositiveSmallIntegerField('Нейроэндокринный синдром', choices=YESNODONTKNOW, default=NO)
    chronic_tonsillitis = models.PositiveSmallIntegerField('Хронический тонзиллит', choices=YESNODONTKNOW, default=NO)
    myocardial_dystrophy = models.PositiveSmallIntegerField('Миокардиодистрофия', choices=YESNODONTKNOW, default=NO)

    def __str__(self):
        return self.name2

    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'