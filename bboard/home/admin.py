from django.contrib import admin

from .models import Bb, Rubric
# Register your models here.
class BbAdmin(admin.ModelAdmin):
    list_display = ['rubric', 'title', 'description', 'price', 'published']
    list_display_links = ['title', 'description']
    search_fields = ['title', 'description']

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
