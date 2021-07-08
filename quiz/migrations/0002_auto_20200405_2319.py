# Generated by Django 3.0.3 on 2020-04-05 20:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='mcqquestion',
            options={'verbose_name': 'Вопрос с несколькими вариантами ответов', 'verbose_name_plural': 'Вопросы с несколькими вариантами ответов'},
        ),
        migrations.AlterModelOptions(
            name='progress',
            options={'verbose_name': 'Прогресс пользователя', 'verbose_name_plural': 'Прогресс пользователя'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['lesson'], 'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='sitting',
            options={'permissions': (('view_sittings', 'Может просматривать оконченные тесты'),)},
        ),
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.CharField(help_text='Введите текст ответа', max_length=1000, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(default=False, help_text='Это правильный ответ?', verbose_name='Правильно'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.MCQQuestion', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='mcqquestion',
            name='answer_order',
            field=models.CharField(blank=True, choices=[('content', 'Содержание'), ('none', 'Ничего'), ('random', 'Случайно')], help_text='Порядок отображения вопросов', max_length=30, null=True, verbose_name='Порядок вопросов'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='correct_answer',
            field=models.CharField(max_length=10, verbose_name='Правильные ответы'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='score',
            field=models.CharField(max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Баллы'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='wrong_answer',
            field=models.CharField(max_length=10, verbose_name='Неправильные ответы'),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.CharField(help_text='Введите текст вопроса, который должен отобразиться', max_length=1000, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='explanation',
            field=models.TextField(blank=True, help_text='Объяснение показывается после того, как дан ответ на вопрос', max_length=2000, verbose_name='Объяснение'),
        ),
        migrations.AlterField(
            model_name='question',
            name='figure',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d', verbose_name='Рисунок'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answers_at_end',
            field=models.BooleanField(default=False, help_text='Правильный ответ НЕ показан после вопроса. Ответы отображаются после прохождения теста', verbose_name='Ответы в конце'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='draft',
            field=models.BooleanField(blank=True, default=False, help_text='Если отмечено, то не отображается в публичном списке и может быть взято только пользователями с соответствующим правом', verbose_name='Черновик'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='exam_paper',
            field=models.BooleanField(default=False, help_text='Если отмечено, результаты каждой попытки пользователя будет сохранен', verbose_name='Экзаменационный лист'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='fail_text',
            field=models.TextField(blank=True, help_text='Текст при не выполнении теста', verbose_name='Текст в случае неудачи'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='max_questions',
            field=models.PositiveIntegerField(blank=True, help_text='Количество вопросов, на которые должны быть даны ответы при каждой попытке', null=True, verbose_name='Максимальное количество вопросов'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='pass_mark',
            field=models.SmallIntegerField(blank=True, default=0, help_text='Процент правильных ответов для прохождения теста', validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Pass Mark'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='random_order',
            field=models.BooleanField(default=False, help_text='Отображать вопросы в случайном порядке или в порядке добавления?', verbose_name='Случайная порядок'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='single_attempt',
            field=models.BooleanField(default=False, help_text='Если отмечено, пользователю будет разрешена только одна попытка', verbose_name='Единственная попытка'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='success_text',
            field=models.TextField(blank=True, help_text='Отображается, если пользователь успешно прошел тест', verbose_name='Текст при успешном выполнении теста'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='url',
            field=models.SlugField(help_text='url теста', max_length=60, verbose_name='url теста'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='complete',
            field=models.BooleanField(default=False, verbose_name='Завершен'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='current_score',
            field=models.IntegerField(verbose_name='Текущий балл'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Окончание'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='incorrect_questions',
            field=models.CharField(blank=True, max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Вопросы, на которые дан неверный ответ'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='question_list',
            field=models.CharField(max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Список вопросов'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='question_order',
            field=models.CharField(max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Порядок вопросов'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz', verbose_name='Тест'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='start',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Начало'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='user_answers',
            field=models.TextField(blank=True, default='{}', verbose_name='Ответы пользователя'),
        ),
    ]