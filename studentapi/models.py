from pydoc import describe
from django.db import models
from simple_history.models import HistoricalRecords

class Place(models.Model):
    study_place_name = models.CharField( verbose_name='Название места учебы', max_length=100, unique=True)
    address = models.CharField(verbose_name='Адрес',max_length=100 )
    since = models.DateTimeField( verbose_name='Дата открытия', max_length=100 )
    work_till = models.TimeField(verbose_name='Рабтает до:')

    history = HistoricalRecords()

    def __str__(self):
        return self.study_place_name

    class Meta:
        verbose_name = 'Место обучения'
        verbose_name_plural = 'Места обучения'

class Projects(models.Model):
    title = models.CharField( verbose_name='Название проекта', max_length=100)
    description = models.TextField(verbose_name='Инофрмация о проекте')
    curator = models.CharField( verbose_name='Куратор проекта', max_length=100)
    deadline = models.DateTimeField(verbose_name='Дедлайн проекта')

    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class Student(models.Model):
    name = models.CharField( verbose_name='ФИО', max_length=100)
    group = models.IntegerField(verbose_name='Группа')
    about = models.TextField(verbose_name='О студенте')
    course = models.IntegerField( verbose_name='Курс')
    project =  models.ManyToManyField(Projects, verbose_name='Проект студента')
    place = models.ManyToManyField(Place, verbose_name='Место обучения')

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class Lesson(models.Model):
    name = models.CharField( verbose_name='Название предмета', max_length=100) 
    lecturer = models.CharField(verbose_name='Преподаватель', max_length=100)
    student = models.ManyToManyField(Student, verbose_name='Ученик')
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмет'

