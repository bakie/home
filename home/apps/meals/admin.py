from django.contrib import admin
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Recipe, Ingredient, Unit, RecipeIngredient, Menu


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0


class RecipesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple(Ingredient, False)},
    }
    inlines = [
        RecipeIngredientInline,
    ]


admin.site.register(Recipe, RecipesAdmin)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(Menu)
