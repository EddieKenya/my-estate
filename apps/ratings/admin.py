from django.contrib import admin

# Register your models here.
from. models import Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ["customer","agent", "rating"]


admin.site.register(Rating, RatingAdmin)



