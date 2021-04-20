# Generated by Django 3.1 on 2021-04-16 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryNPA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория НПА')),
                ('data_cr', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Категория НПА',
            },
        ),
        migrations.CreateModel(
            name='CategoryOC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Категория')),
                ('data_cr', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Категория ОС',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('contacts', models.CharField(max_length=3000, verbose_name='Контакты')),
            ],
            options={
                'verbose_name': 'Контвкты',
            },
        ),
        migrations.CreateModel(
            name='ContentOrganizationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, verbose_name='Наименовение категории')),
                ('data_cr', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Категория организации контента',
            },
        ),
        migrations.CreateModel(
            name='CorruptionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория антикоррупционной деятельности',
            },
        ),
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Организации')),
                ('contacts', models.CharField(max_length=3000, verbose_name='Контакты')),
            ],
            options={
                'verbose_name': 'Справочник',
            },
        ),
        migrations.CreateModel(
            name='Leadership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', models.CharField(max_length=400, verbose_name='Инициалы')),
                ('title', models.CharField(max_length=500, verbose_name='Должность')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('Fax', models.CharField(max_length=50, verbose_name='Fax')),
                ('mail', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Руковотство',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=3000, verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=3000, verbose_name='Под заголовок')),
                ('img', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='фото')),
                ('file', models.FileField(blank=True, null=True, upload_to='document', verbose_name='документ')),
                ('text', models.TextField(max_length=5000, verbose_name='Текст')),
                ('video', models.URLField()),
                ('status', models.CharField(choices=[('unprocessed', 'unprocessed'), ('published', 'published'), ('declined', 'declined')], default='unprocessed', max_length=45, verbose_name='status')),
                ('data_cr', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='OrganizationStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', models.CharField(max_length=400, verbose_name='Инициалы')),
                ('title', models.CharField(max_length=500, verbose_name='Должность')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('Fax', models.CharField(max_length=50, verbose_name='Fax')),
                ('mail', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('data_cr', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Структура организации',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
                ('data_cr', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Положение',
            },
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('data_cr', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directions', models.CharField(max_length=300, verbose_name='Направление')),
                ('document_type', models.CharField(max_length=300, verbose_name='Вид документа')),
                ('date', models.DateField(verbose_name='Дата')),
                ('author', models.CharField(max_length=300, verbose_name='Автор')),
                ('number', models.IntegerField(verbose_name='Номер документа')),
                ('file', models.FileField(upload_to='study', verbose_name='Файл')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование Файла')),
                ('data_cr', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Исследования',
            },
        ),
        migrations.CreateModel(
            name='SUR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('file', models.FileField(upload_to='doc', verbose_name='файл')),
                ('date', models.DateField(verbose_name='Дата')),
                ('date_cr', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'ЦУР',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('data', models.DateField(verbose_name='Дата')),
                ('text', models.CharField(max_length=3000, verbose_name='Текст')),
                ('file', models.FileField(blank=True, null=True, upload_to='doc', verbose_name='Документ')),
                ('data_cr', models.DateField(auto_now_add=True, verbose_name='дата создания')),
            ],
            options={
                'verbose_name': 'Вкансии',
            },
        ),
        migrations.CreateModel(
            name='StructureOC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', models.CharField(max_length=300, verbose_name='Инициалы')),
                ('Position', models.CharField(max_length=300, verbose_name='Должность и место работы')),
                ('area_of_expertise', models.CharField(max_length=300, verbose_name='Область экспертизы')),
                ('phone', models.CharField(max_length=300, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('data_cr', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.categoryoc', verbose_name='Категория ОС')),
            ],
            options={
                'verbose_name': 'Состав ОС',
            },
        ),
        migrations.CreateModel(
            name='RegulationsOC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=400, verbose_name='Описание')),
                ('file', models.FileField(upload_to='OC', verbose_name='Фаил')),
                ('data_cr', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related', to='webapp.categoryoc', verbose_name='Категория ОС')),
            ],
            options={
                'verbose_name': 'Нормативно-правовые акты',
            },
        ),
        migrations.CreateModel(
            name='RecommendationOC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Наименование')),
                ('file', models.FileField(upload_to='OC', verbose_name='Фаил')),
                ('data_cr', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='webapp.categoryoc', verbose_name='Категория ОС')),
            ],
            options={
                'verbose_name': 'Рекомендации ОС',
            },
        ),
        migrations.CreateModel(
            name='NPA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Заголово')),
                ('subtitle', models.CharField(max_length=300, verbose_name='Под зоголовок')),
                ('document_type', models.CharField(max_length=300, verbose_name='Вид документа')),
                ('date', models.DateField(verbose_name='Дата')),
                ('file', models.FileField(upload_to='doc', verbose_name='Документ')),
                ('text', models.TextField(max_length=5000, verbose_name='Содержание')),
                ('data_cr', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_to_content', to='webapp.categorynpa', verbose_name='Категория НПА')),
            ],
            options={
                'verbose_name': 'НПА',
            },
        ),
        migrations.CreateModel(
            name='Corruption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='Заголовок')),
                ('document_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Тип токумента')),
                ('file', models.FileField(upload_to='doc', verbose_name='Файл')),
                ('data_cr', models.DateField(auto_now_add=True, verbose_name='Дата Создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='webapp.corruptioncategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Антикоррупционная деятельность',
            },
        ),
        migrations.CreateModel(
            name='ContentOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=5000, verbose_name='Текст')),
                ('img', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='фото')),
                ('video', models.URLField(blank=True, null=True, verbose_name='ссылка на фидео')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('data_cr', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_to_content', to='webapp.contentorganizationcategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Сонтент организации',
            },
        ),
    ]
