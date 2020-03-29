from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.db import transaction
from . import models
from . import forms


# Create your views here.
def index(request):
    context = {}
    return render(request, 'meals_index.html', context)


class IngredientList(ListView):
    model = models.Ingredient
    template_name = 'meals_ingredient_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ingredient_objects = []
        for ingredient in self.object_list:
            modal = {
                'title': 'Delete ingredient',
                'id': 'delete-ingredient-modal-%s' % str(ingredient.id),
                'body': 'Are you sure you want to delete %s ?' % ingredient.name,
                'post_url': reverse('meals:ingredient_delete', kwargs={'pk': ingredient.id})
            }
            ingredient_objects.append({'ingredient': ingredient, 'modal': modal})
        context['ingredient_objects'] = ingredient_objects
        return context


class IngredientCreate(CreateView):
    model = models.Ingredient
    form_class = forms.IngredientForm
    template_name = 'snippets/form.html'
    success_url = '/meals/ingredient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = True
        context['type'] = "Ingredient"
        return context


class IngredientUpdate(UpdateView):
    model = models.Ingredient
    form_class = forms.IngredientForm
    template_name = 'snippets/form.html'
    success_url = '/meals/ingredient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        context['type'] = "Ingredient"
        return context


class IngredientDeleteView(DeleteView):
    model = models.Ingredient
    success_url = '/meals/ingredient'
    success_message = "Successfully deleted %(name)s"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(IngredientDeleteView, self).delete(request, *args, **kwargs)


class MenuList(ListView):
    model = models.Menu
    template_name = 'meals_menu_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_objects = []
        for menu in self.object_list:
            modal = {
                'title': 'Delete menu',
                'id': 'delete-menu-modal-%s' % str(menu.id),
                'body': 'Are you sure you want to delete the menu for week %s ?' % str(menu.week_number),
                'post_url': reverse('meals:menu_delete', kwargs={'pk': menu.id})
            }
            menu_objects.append({'menu': menu, 'modal': modal})
        context['menu_objects'] = menu_objects
        return context


class MenuDeleteView(DeleteView):
    model = models.Menu
    success_url = '/meals/menu'
    success_message = "Successfully deleted %(name)s"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(MenuDeleteView, self).delete(request, *args, **kwargs)


class RecipeList(ListView):
    model = models.Recipe
    template_name = 'meals_recipe_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_objects = []
        for recipe in self.object_list:
            modal = {
                'title': 'Delete recipe',
                'id': 'delete-recipe-modal-%s' % str(recipe.id),
                'body': 'Are you sure you want to delete %s ?' % recipe.name,
                'post_url': reverse('meals:recipe_delete', kwargs={'pk': recipe.id})
            }
            recipe_objects.append({'recipe': recipe, 'modal': modal})
        context['recipe_objects'] = recipe_objects
        return context


class RecipeCreate(CreateView):
    model = models.Recipe
    form_class = forms.RecipeForm
    template_name = 'snippets/formset.html'

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super(RecipeCreate, self).form_valid(form)

    def get_success_url(self):
        return '/meals/recipe'

    def get_context_data(self, **kwargs):
        data = super(RecipeCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = forms.RecipeFormSet(self.request.POST)
        else:
            data['formset'] = forms.RecipeFormSet()
            data['formset_prefix'] = 'ingredientsformset'
        return data


class RecipeDeleteView(DeleteView):
    model = models.Recipe
    success_url = '/meals/recipe'
    success_message = "Successfully deleted %(name)s"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(RecipeDeleteView, self).delete(request, *args, **kwargs)
