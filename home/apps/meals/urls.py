from django.urls import path
from . import views

app_name = 'meals'

urlpatterns = [
    path('', views.index, name='index'),
    path('ingredient/', views.IngredientList.as_view(), name='ingredient_list'),
    path('ingredient/add/', views.IngredientCreate.as_view(), name='ingredient_add'),
    path('ingredient/<int:pk>/update', views.IngredientUpdate.as_view(), name='ingredient_update'),
    path('ingredient/<int:pk>/delete', views.IngredientDeleteView.as_view(), name='ingredient_delete'),
    path('menu/', views.MenuList.as_view(), name='menu_list'),
    path('menu/<int:pk>/delete', views.MenuDeleteView.as_view(), name='menu_delete'),
    path('recipe/', views.RecipeList.as_view(), name='recipe_list'),
    path('recipe/add/', views.RecipeCreate.as_view(), name='recipe_add'),
    path('recipe/<int:pk>/delete', views.RecipeDeleteView.as_view(), name='recipe_delete')
]
