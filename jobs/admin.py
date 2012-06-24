from django.contrib import admin
from jobs.models import *


class ApplicationPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ApplicationPageInline(admin.StackedInline):
    model = Application.pages.through


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'employer')
    inlines = [
        ApplicationPageInline
    ]
    exclude = ('pages',)


admin.site.register(Employer)
admin.site.register(ApplicationPage, ApplicationPageAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(GenericContent)
admin.site.register(Link)
admin.site.register(Reference)
admin.site.register(WorkExperience)
admin.site.register(Study)
admin.site.register(Skill)
