import datetime

from .models import Articles, Complaints
from django.forms import ModelForm
from django import forms
from django.db import models

DOY = ('1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947',
       '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955',
       '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963',
       '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971',
       '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979',
       '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
       '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
       '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027')

class ArticlesForm(ModelForm):
    title = forms.ChoiceField(label='Название', choices=((1, 'Пациент'), (2, '--')))
    name = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={'class': 'my-field'}))
    date_of_birth = forms.DateField(label='Дата рождения', widget=forms.SelectDateWidget(years=DOY, attrs={'class': 'my-field'}))
    sex = forms.ChoiceField(label='Пол пациента', choices=((1, 'Мужской'), (2, 'Женский')))
    insurance = forms.CharField(label='Страховая организация', widget=forms.TextInput(attrs={'class': 'my-field'}))
    policy = forms.CharField(label='Страховое свидетельство', widget=forms.TextInput(attrs={'class': 'my-field'}))
    address = forms.CharField(label='Домашний адрес', widget=forms.TextInput(attrs={'class': 'my-field'}))
    number_phone = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'my-field'}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'my-field'}))
    parent_name = forms.CharField(label='ФИО родителя', widget=forms.TextInput(attrs={'class': 'my-field'}))
    parent_number_phone = forms.CharField(label='Номер телефона родителя', widget=forms.TextInput(attrs={'class': 'my-field'}))
    parent_email = forms.EmailField(label='Электронная почта родителя', widget=forms.EmailInput(attrs={'class': 'my-field'}))
    nation = forms.ChoiceField(label='Нация пациента', choices=((1, 'Русские'), (2, 'Украинцы'), (3, 'Немцы'), (4, 'Казахи'), (5, 'Белорусы'), (6, 'Алтайцы'), (7, 'Кумандинцы'), (8, 'Татары'), (9, 'ДРУГАЯ')))
    mother_nation = forms.ChoiceField(label='Нация матери пациента', choices=((1, 'Русские'), (2, 'Украинцы'), (3, 'Немцы'), (4, 'Казахи'), (5, 'Белорусы'), (6, 'Алтайцы'), (7, 'Кумандинцы'), (8, 'Татары'), (9, 'ДРУГАЯ')))
    father_nation = forms.ChoiceField(label='Нация отца пациента', choices=((1, 'Русские'), (2, 'Украинцы'), (3, 'Немцы'), (4, 'Казахи'), (5, 'Белорусы'), (6, 'Алтайцы'), (7, 'Кумандинцы'), (8, 'Татары'), (9, 'ДРУГАЯ')))
    registration_date = forms.DateField(label='Дата регистрации пациента', widget=forms.SelectDateWidget(attrs={'class': 'my-field'}))

    class Meta:
        model = Articles
        fields = ['title', 'name', 'date_of_birth', 'sex', 'insurance', 'policy', 'address', 'number_phone', 'email',
                  'parent_name', 'parent_number_phone', 'parent_email', 'nation', 'mother_nation', 'father_nation', 'registration_date']

class ComplaintsForm(ModelForm):
    #name2 = forms.ChoiceField(choices=Complaints.objects.order_by('articles_id'))
    name2 = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={'class': 'my-field'}))
    date_receipt = forms.DateField(label='Дата приёма', widget=forms.SelectDateWidget(attrs={'class': 'my-field'}))

    # Жалобы
    nosebleeds = forms.ChoiceField(label='Носовые кровотечения', choices=((1, 'Справа'), (2, 'Слева'), (3, 'Справа и слева'), (4, 'Нет')))
    nosebleeds_per_month = forms.CharField(label='Количество носовых кровотечений в месяц', widget=forms.TextInput(attrs={'class': 'my-field'}))
    abundant_periods = forms.ChoiceField(label='Обильные месячные', choices=((1, 'Нет'), (2, 'Да')))
    bleeding_gums = forms.ChoiceField(label='Кровоточивость дёсен', choices=((1, 'Нет'), (2, 'Да')))
    bruising = forms.ChoiceField(label='Синячковость', choices=((1, 'Нет'), (2, 'Да')))
    other_bleeding = forms.CharField(label='Другая кровоточивость', widget=forms.TextInput(attrs={'class': 'my-field'}))
    duration_of_bleeding = forms.IntegerField(label='Длительность кровоточивости(мин)')
    fainting = forms.ChoiceField(label='Обмороки', choices=((1, 'Нет'), (2, 'Да')))
    dizziness = forms.ChoiceField(label='Головокружения', choices=((1, 'Нет'), (2, 'Да')))
    heart_pain = forms.ChoiceField(label='Боль в области сердца', choices=((1, 'Нет'), (2, 'Да')))
    others = forms.CharField(label='Другие', widget=forms.TextInput(attrs={'class': 'my-field'}))
    first_appearance = forms.IntegerField(label='Первое появление, возраст')
    provocation_of_nosebleeds = forms.ChoiceField(label='Провокация носовых кровотечений', choices=((1, 'Утро'), (2, 'День'), (3, 'Ночь'), (4, 'Вечер'), (5, 'Физ нагрузка'), (6, 'Умственная нагрузка'), (7, 'Стресс'), (8, 'Весна'), (9, 'Осень')))

    # У родственников
    nosebleeds2 = forms.ChoiceField(label='Носовые кровотечения', choices=((1, 'Справа'), (2, 'Слева'), (3, 'Справа и слева'), (4, 'Нет')))
    abundant_periods2 = forms.ChoiceField(label='Обильные месячные', choices=((1, 'Нет'), (2, 'Да')))
    bleeding_gums2 = forms.ChoiceField(label='Кровоточивость дёсен', choices=((1, 'Нет'), (2, 'Да')))
    bruising2 = forms.ChoiceField(label='Синячковость', choices=((1, 'Нет'), (2, 'Да')))
    other_bleeding2 = forms.CharField(label='Другая кровоточивость', widget=forms.TextInput(attrs={'class': 'my-field'}))
    father_infarct = forms.ChoiceField(label='Был ли у отца инфаркт, инсульт, тромбоз до 55 лет', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    mother_infarct = forms.ChoiceField(label='Был ли у матери инфаркт, инсульт, тромбоз до 65 лет', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    grand_infarct = forms.ChoiceField(label='Был ли у деда/бабушки инфаркт, инсульт, тромбоз, до 65 лет', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))

    # Перенесенные заболевания | Сопутствующие заболевания | Соматические заболевания
    myocardial_infarction = forms.ChoiceField(label='Инфаркт миокарда', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    stroke = forms.ChoiceField(label='Инсульт (ТИА, ОНМК)', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    thrombosis = forms.ChoiceField(label='Тромбозы', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    heart_surgery = forms.ChoiceField(label='Операции на сердце и сосудах', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))

    cancer_disease = forms.ChoiceField(label='Онкологическое заболевание', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    hypertonic_disease = forms.ChoiceField(label='Гипертоническая болезнь', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    work_of_the_heart = forms.ChoiceField(label='Перебои в работе сердца', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    atrial_fibrillation = forms.ChoiceField(label='Фибрилляция предсердий', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    diabetes = forms.ChoiceField(label='Сахарный диабет', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    varicose_veins = forms.ChoiceField(label='Варикозная болезнь', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    flat_feet = forms.ChoiceField(label='Плоскостопие/гипермобильность суставов', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    fainting2 = forms.ChoiceField(label='Обмороки', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    dizziness2 = forms.ChoiceField(label='Головокружения', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    obesity = forms.ChoiceField(label='Ожирение', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))

    bronchial_asthma = forms.ChoiceField(label='Бронхиальная астма', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    ari_times_a_year = forms.ChoiceField(label='ОРИ > 4 раз в год', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    diseases_of_the_thyroid_gland = forms.ChoiceField(label='Заболевания щитовидной железы', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    chronic_pyelonephritis = forms.ChoiceField(label='Хронический пиелонефрит', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    chronic_gastritis = forms.ChoiceField(label='Хронический гастрит', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    arrhythmia = forms.ChoiceField(label='Аритмия', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    vegetovascular_dystonia = forms.ChoiceField(label='Вегето-сосудистая дистония', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    migraine = forms.ChoiceField(label='Мигрени', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    osteochondrosis = forms.ChoiceField(label='Остеохондроз', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    loss_of_visual_fields = forms.ChoiceField(label='Выпадение полей зрения', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    heart_defects = forms.ChoiceField(label='Пороки сердца', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    neuroendocrine_syndrome = forms.ChoiceField(label='Нейроэндокринный синдром', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    chronic_tonsillitis = forms.ChoiceField(label='Хронический тонзиллит', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))
    myocardial_dystrophy = forms.ChoiceField(label='Миокардиодистрофия', choices=((1, 'Нет'), (2, 'Да'), (3, 'Не знаю')))

    class Meta:
        model = Complaints
        fields = ['name2', 'date_receipt', 'nosebleeds', 'nosebleeds_per_month', 'abundant_periods', 'bleeding_gums', 'bruising', 'other_bleeding', 'duration_of_bleeding', 'fainting',
                  'dizziness', 'heart_pain', 'others', 'first_appearance', 'provocation_of_nosebleeds', 'nosebleeds2', 'abundant_periods2', 'bleeding_gums2',
                  'bruising2', 'other_bleeding2', 'father_infarct', 'mother_infarct', 'grand_infarct', 'myocardial_infarction', 'stroke', 'thrombosis', 'heart_surgery']