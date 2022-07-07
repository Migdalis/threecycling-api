from unicodedata import category
from django.http import HttpResponse, Http404
from api.models.product import Product
from api.models.category import Category
from api.models.user import User
from django.utils import timezone


def get_products(request):
    """ Get all products """
    return HttpResponse(Product.objects.all())


def get_product(request, product_id):
    """ Get a product by id """
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return HttpResponse(product)


def get_product_category(request, category_id):
    """ Get products by category """
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404("Category does not exist")
    return HttpResponse(category.product_set.all())


def get_product_category_name(request, category_name):
    """ Get product by category name """
    try:
        category = Category.objects.get(name=category_name)
    except Category.DoesNotExist:
        raise Http404("Category name does not exist")
    return HttpResponse(category.product_set.all())


def get_product_user(request, user_id):
    """ Get product by user id """
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return HttpResponse(user.product_set.all())


def create_product(request, user_id):
    """ Create a new product """
    try:
        category_obj = Category.objects.get(name=request.POST["category"])
        user_obj = User.objects.get(pk=user_id)
    except Category.DoesNotExist:
        raise Http404("category must be a Category instance")
    except User.DoesNotExist:
        raise Http404("user must be a User instance")
    else:
        return HttpResponse(Product.objects.create(
            name=request.POST["name"],
            category=category_obj,
            description=request.POST["description"],
            user=user_obj,
            price=request.POST["price"],
            image="",
            created_at=timezone.now()
        ))
