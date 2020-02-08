from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    ingredients = models.ManyToManyField("Ingredient", through="RecipeIngredient", related_name="recipes")

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING, related_name="recipe_ingredients")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    unit = models.ForeignKey(Unit, default=0, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s %s" % (self.amount, self.ingredient)


class Menu(models.Model):
    week_number = models.IntegerField(blank=False)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return "Menu for week %s" % self.week_number
