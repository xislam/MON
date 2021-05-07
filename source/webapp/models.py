from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

from accounts.models import User


class StatusChoice(models.TextChoices):
    UNPROCESSED = 'unprocessed', _('unprocessed')
    PUBLISHED = 'published', _('published')
    DECLINED = 'declined', _('declined')


class News(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=3000, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=3000, verbose_name='Под заголовок')
    img = models.ImageField(null=True, blank=True, verbose_name='фото', upload_to="img")
    file = models.FileField(null=True, blank=True, verbose_name='документ', upload_to="document")
    text = RichTextField()
    video = models.URLField()
    status = models.CharField(_('status'), max_length=45,
                              choices=StatusChoice.choices,
                              default=StatusChoice.UNPROCESSED)
    data_cr = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    director = models.OneToOneField('accounts.User', models.SET_NULL, null=True,
                                    related_name='own_news', verbose_name=_('director'))
    employee = models.OneToOneField('accounts.User', models.SET_NULL, null=True, verbose_name=_('employee'),
                                    related_name='emp')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class ContentOrganizationCategory(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    category = models.CharField(max_length=200, verbose_name='Наименовение категории')
    data_cr = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория организации контента'
        verbose_name_plural = 'Категория организации контента'


class ContentOrganization(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(ContentOrganizationCategory, on_delete=models.CASCADE,
                                 related_name='related_to_content', verbose_name='Категория')
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = RichTextField()
    img = models.ImageField(null=True, blank=True, verbose_name='фото', upload_to="img")
    video = models.URLField(null=True, blank=True, verbose_name='ссылка на фидео')
    create_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Контент организации'
        verbose_name_plural = 'Контент организации'


class OrganizationStructure(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    initials = models.CharField(max_length=400, verbose_name='Инициалы')
    title = models.CharField(max_length=500, verbose_name='Должность')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    Fax = models.CharField(max_length=50, verbose_name='Fax')
    mail = models.EmailField(verbose_name='E-mail')
    data_cr = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Структура организации'
        verbose_name_plural = 'Структура организации'


class Organization(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=300, verbose_name='Наименование')
    director = models.OneToOneField('accounts.User', models.SET_NULL, null=True,
                                    related_name='own_organization', verbose_name=_('director'))
    employee = models.OneToOneField('accounts.User', models.SET_NULL, null=True, verbose_name=_('employee'),
                                    related_name="em")


class CategoryNPA(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(verbose_name="Категория НПА", max_length=100)
    data_cr = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория НПА'
        verbose_name_plural = 'Категория НПА'


class NPA(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(CategoryNPA, on_delete=models.CASCADE,
                                 related_name='related_to_content', verbose_name='Категория НПА')
    title = models.CharField(verbose_name="Заголово", max_length=300)
    subtitle = models.CharField(verbose_name="Под зоголовок", max_length=300)
    document_type = models.CharField(max_length=300, verbose_name='Вид документа')
    date = models.DateField(verbose_name='Дата')
    file = models.FileField(verbose_name='Документ', upload_to='doc')
    text = RichTextField()
    data_cr = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    director = models.OneToOneField('accounts.User', models.SET_NULL, null=True,
                                    related_name='own_npa', verbose_name=_('director'))
    employee = models.OneToOneField('accounts.User', models.SET_NULL, null=True, verbose_name=_('employee'),
                                    related_name="employee")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'НПА'
        verbose_name_plural = 'НПА'


class Leadership(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    initials = models.CharField(max_length=400, verbose_name='Инициалы')
    title = models.CharField(max_length=500, verbose_name='Должность')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    Fax = models.CharField(max_length=50, verbose_name='Fax')
    mail = models.EmailField(verbose_name='E-mail')

    def __str__(self):
        return self.initials

    class Meta:
        verbose_name = 'Руковотство'
        verbose_name_plural = 'Руковотство'


class Structure(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='Наименование')
    data_cr = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name


class Position(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    description = RichTextField()
    data_cr = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Положение'
        verbose_name_plural = 'Положение'


class Study(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    directions = models.CharField(max_length=300, verbose_name='Направление')
    document_type = models.CharField(max_length=300, verbose_name='Вид документа')
    date = models.DateField(verbose_name='Дата')
    author = models.CharField(max_length=300, verbose_name='Автор')
    number = models.IntegerField(verbose_name='Номер документа')
    file = models.FileField(verbose_name="Файл", upload_to="study")
    name = models.CharField(max_length=100, verbose_name='Наименование Файла')
    data_cr = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    director = models.OneToOneField('accounts.User', models.SET_NULL, null=True,
                                    related_name='own_study', verbose_name=_('director'))
    employee = models.OneToOneField('accounts.User', models.SET_NULL, null=True, verbose_name=_('employee'),
                                    related_name="loyee")

    def __str__(self):
        return self.directions

    class Meta:
        verbose_name = 'Исследования'
        verbose_name_plural = 'Исследования'


class Advertisement(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    data = models.DateField(verbose_name='Дата')
    text = RichTextField()
    file = models.FileField(null=True, blank=True, verbose_name="Файл", upload_to='boc')
    data_cr = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявления"
        verbose_name_plural = 'Объявления'


class CategoryOC(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=300, verbose_name='Категория')
    data_cr = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория ОС"
        verbose_name_plural = 'Категория ОС'


class StructureOC(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(CategoryOC, on_delete=models.CASCADE, verbose_name='Категория ОС')
    initials = models.CharField(max_length=300, verbose_name='Инициалы')
    position = models.CharField(max_length=300, verbose_name='Должность и место работы')
    area_of_expertise = models.CharField(max_length=300, verbose_name='Область экспертизы')
    phone = models.CharField(max_length=300, verbose_name="Телефон")
    email = models.EmailField(verbose_name='Почта')
    data_cr = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.initials

    class Meta:
        verbose_name = "Состав ОС"
        verbose_name_plural = 'Состав ОС'


class RegulationsOC(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(CategoryOC, on_delete=models.CASCADE,
                                 related_name='related', verbose_name='Категория ОС')
    description = models.CharField(max_length=400, verbose_name="Описание")
    file = models.FileField(verbose_name="Фаил", upload_to="OC")
    data_cr = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Нормативно-правовые акты"
        verbose_name_plural = 'Нормативно-правовые акты'


class RecommendationOC(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(CategoryOC, on_delete=models.CASCADE,
                                 related_name='category', verbose_name='Категория ОС')
    name = models.CharField(max_length=300, verbose_name="Наименование")
    file = models.FileField(verbose_name="Фаил", upload_to='OC')
    data_cr = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рекомендации ОС"
        verbose_name_plural = 'Рекомендации ОС'


class CorruptionCategory(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=300, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория антикоррупционной деятельности"
        verbose_name_plural = "Категория антикоррупционной деятельности"


class Corruption(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(CorruptionCategory, on_delete=models.CASCADE,
                                 related_name='category', verbose_name='Категория')
    title = models.CharField(max_length=400, verbose_name="Заголовок")
    document_type = models.CharField(null=True, blank=True, max_length=200, verbose_name="Тип токумента")
    file = models.FileField(verbose_name='Файл', upload_to="doc")
    data_cr = models.DateField(auto_now_add=True, verbose_name='Дата Создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Антикоррупционная деятельность"
        verbose_name_plural = "Антикоррупционная деятельность"


class VacancyCategory(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=300, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория вакансии"
        verbose_name_plural = "Категория вакансии"


class Vacancy(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=500, verbose_name="Заголовок")
    data = models.DateField(verbose_name='Дата')
    text = models.CharField(max_length=3000, verbose_name='Текст')
    file = models.FileField(null=True, blank=True, verbose_name="Документ", upload_to="doc")
    data_cr = models.DateField(auto_now_add=True, verbose_name="дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вкансии"
        verbose_name_plural = "Вкансии"


class Contacts(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name="заголовок")
    contacts = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Directory(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=300, verbose_name="Организации")
    contacts = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочник'


class SUR(models.Model):
    user = models.ForeignKey(User, verbose_name=u"пользователь", on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=500, verbose_name="Заголовок")
    file = models.FileField(verbose_name='файл', upload_to="doc")
    date = models.DateField(verbose_name='Дата')
    date_cr = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ЦУР'
        verbose_name_plural = 'ЦУР'
