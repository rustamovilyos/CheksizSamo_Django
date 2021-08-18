from django.contrib import admin
from .models import Janrlar, Kitoblar


class JanrAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomi')


class KitobAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomi', 'muallif', 'rasm', 'fayl', 'audio', 'nashr_yili')


admin.site.register(Janrlar, JanrAdmin)
admin.site.register(Kitoblar, KitobAdmin)
