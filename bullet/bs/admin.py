from django.contrib import admin
from .models import Color,Bul
# Register your models here.
class BulAdmin(admin.ModelAdmin):
    list_display = ['bul_content',
                    'timestamp',
                    'bul_color',
                    'bul_size',
                    'if_shown',]
    search_fields = ['bul_content','timestamp']
    class Meta:
        model = Bul

class ColorAdmin(admin.ModelAdmin):
    list_display = ['color_name','color_value']
    class Meta:
        model = Color
admin.site.register(Bul,BulAdmin)
admin.site.register(Color,ColorAdmin)