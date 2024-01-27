from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe, Product, RecipeProduct

from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products_list.html', {'products': products})


def add_product_to_recipe(request):
    all_products = Product.objects.all()
    all_recipes = Recipe.objects.all()
    context = {
        'all_products': all_products,
        'all_recipes': all_recipes,
    }
    if request.POST:
        product = Product.objects.get(id=request.POST['product'])
        recipe = Recipe.objects.get(id=request.POST['recipe'])
        weight = request.POST['weight']
        recipe_product = RecipeProduct.objects.create(product=product, recipe=recipe, weight=weight)
        recipe_product.save()
        return render(request, 'alert.html')
    return render(request, 'add_reciep.html', context)


def cook_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe_products = recipe.recipeproduct_set.all()

    for rp in recipe_products:
        rp.product.times_prepared += 1
        rp.product.save()

    return render(request, 'alert.html')


def show_recipes_without_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    recipes_without_product = Recipe.objects.exclude(recipeproduct__product=product)
    recipes_less_than_10g = Recipe.objects.filter(recipeproduct__product=product, recipeproduct__weight__lt=10)

    return render(request, 'show_recipes.html',
                  {'recipes_without_product': recipes_without_product, 'recipes_less_than_10g': recipes_less_than_10g})


# views.py

from django.shortcuts import render
from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipe_list.html', context)
