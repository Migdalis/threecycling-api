from django.contrib import admin
from .models.user import User
from .models.category import Category
from .models.product import Product
from .models.offer import Offer


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Offer)
