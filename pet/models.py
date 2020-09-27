import uuid
import datetime

from django.db import models

# Create your models here.

class AnimalKind(models.Model):
    """Вид животного"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256,
            verbose_name="Вид животного")
#    code = models.CharField(max_length=16,
#            verbose_name="Краткий код вида")

    def __str__(self):
        return self.name

class AnimalBreed(models.Model):
    """Порода животного"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256,
            verbose_name="Порода")
    kind = models.ForeignKey(AnimalKind, on_delete=models.CASCADE,
            verbose_name="Вид")
#    code = models.CharField(max_length=16,
#            verbose_name="Краткий код породы")

    def __str__(self):
        return f"{self.kind} - {self.name}"

class Pet(models.Model):
    """Конкретное животное"""
    CONDITION = [
            (10, 'Хорошее'),
            (20, 'Удовлетворительное'),
            (30, 'Плохое'),
    ]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=100,
            verbose_name="Кличка")
    breed = models.ForeignKey(AnimalBreed, on_delete=models.CASCADE,
            verbose_name="Вид и порода")
    description = models.TextField(
            verbose_name="Описание")
    coming_date = models.DateField(default=datetime.date.today,
            verbose_name="Дата поступления")
    condition = models.IntegerField(choices=CONDITION,
            verbose_name="Состояние животного")
    photo = models.ImageField(upload_to='pets_photo', blank=True,
            verbose_name="Фото животного")

    def __str__(self):
        return f"{self.name} - {self.breed}"

