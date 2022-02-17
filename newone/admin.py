from django.contrib import admin
from .models import Lead, User, UserProfile
# Register your models here.
class Search(admin.ModelAdmin):
    search_fields = ['name', 'username' ]
admin.site.register(Lead)
admin.site.register(User, Search)
admin.site.register(UserProfile)

