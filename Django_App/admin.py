from django.contrib import admin
from Django_App.models import Memo

# Register your models here.
class MemoAdmin(admin.ModelAdmin):
    list_display = ('content', 'last_modified')

admin.site.register(Django_App, MemoAdmin)