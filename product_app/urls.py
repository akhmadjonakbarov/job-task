from django.urls import path
from .views import add_product_to_recipe, cook_recipe, show_recipes_without_product, product_list, recipe_list

urlpatterns = [
    path('add_product_to_recipe/', add_product_to_recipe,
         name='add_product_to_recipe'),
    path('cook_recipe/<int:recipe_id>/', cook_recipe, name='cook_recipe'),
    path('show_recipes_without_product/<int:product_id>/', show_recipes_without_product,
         name='show_recipes_without_product'),
    path('', product_list, name='product_list'),  # New URL for product list
    path('recipes/', recipe_list, name='recipe_list'),
    # other paths for your application...
]
