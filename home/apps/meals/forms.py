from django.contrib import admin
from django import forms
from . import models


class IngredientForm(forms.ModelForm):
    class Meta:
        model = models.Ingredient
        fields = ['name']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = models.Recipe
        exclude = ['ingredients']


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = models.RecipeIngredient
        fields = '__all__'


RecipeFormSet = forms.inlineformset_factory(models.Recipe, models.RecipeIngredient, form=RecipeIngredientForm, extra=1,
                                            can_delete=True)

