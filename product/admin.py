
from django.contrib import admin
from product.models import *

MAX_OBJECTS=1

# Register your models here.
admin.site.register(ProductImage)


class ProductImageInline(admin.StackedInline):
  model = ProductImage
  max_num=10
  extra=1
    
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    inlines = [ProductImageInline,]
    list_display = ['name','slug','created_date','updated_date','seller']

@admin.register(MainCategory)
class AdminMainCategory(admin.ModelAdmin):
    list_display = ['name']


@admin.register(SubCategory)
class AdminSubCategory(admin.ModelAdmin):
    list_display = ['name']

@admin.register(AdsSettings)
class AdminAdsSettings(admin.ModelAdmin):
    # list_display = ['name']

    def has_add_permission(self, request):
          if self.model.objects.count() >= MAX_OBJECTS:
               return False
          return super().has_add_permission(request)


admin.site.register(Brand)

admin.site.register(Basket)


admin.site.register(Invoice)

admin.site.register(Notification)


admin.site.register(Comment)



