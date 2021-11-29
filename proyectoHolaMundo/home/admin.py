from django.contrib import admin

from .models import tessue, Paciente

# Register your models here.


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Paciente, PacienteAdmin)


class tessueAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'color', 'inflammation',)
    search_fields = ('temperature',)

admin.site.register(tessue, tessueAdmin)

