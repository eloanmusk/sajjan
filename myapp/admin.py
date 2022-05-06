from django.contrib import admin
from .models import Product

 
admin.site.site_header = "Sajjan and Co."
admin.site.site_title = "Buy Cars at Reasonable Price" 
admin.site.index_title = "Sajjan and Co."


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'desc', 'image')
    search_fields = ('name',)

    def sold_items(self, request, queryset):
        queryset.update(desc="Sold")

    actions = ('sold_items',)
    list_editable = ('price', 'desc',)

admin.site.register(Product, ProductAdmin)
