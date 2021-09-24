from django.contrib import admin

# Register your models here.

from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "Author", "Created_on")
    search_fields= ["Contents"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "description")
    

admin.site.register(Post,PostAdmin)
admin.site.register(Category, CategoryAdmin)



