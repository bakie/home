from django.urls import path
from . import views

app_name = 'meals'

urlpatterns = [
    path('', views.index, name='index'),
    path('ingredient/', views.IngredientList.as_view(), name='ingredient_list'),
    path('ingredient/<int:pk>/delete', views.IngredientDeleteView.as_view(), name='ingredient_delete'),
    path('menu/', views.MenuList.as_view(), name='menu_list'),
    path('menu/<int:pk>/delete', views.MenuDeleteView.as_view(), name='menu_delete'),
    path('recipe/', views.RecipeList.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/delete', views.RecipeDeleteView.as_view(), name='recipe_delete')
]
