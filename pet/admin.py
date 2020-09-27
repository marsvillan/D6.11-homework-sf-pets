from django.contrib import admin
from .models import AnimalKind, AnimalBreed, Pet

# Register your models here.
@admin.register(AnimalKind)
class AdminAnimalKind(admin.ModelAdmin):
    readonly_fields = ['id']
    pass

@admin.register(AnimalBreed)
class AdminAnimalBreed(admin.ModelAdmin):
    readonly_fields = ['id']
    pass

@admin.register(Pet)
class AdminPet(admin.ModelAdmin):
    readonly_fields = ['id']
    pass
