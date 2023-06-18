from django.contrib import admin
from .models import *

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ["id","name","category"]
    list_display_links=["id"]
    list_filter=["category"]
    search_fields=["name","category__name"]
    # list_per_page=2
    list_editable=["name"]


admin.site.register(Movies,MovieAdmin)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Watched)