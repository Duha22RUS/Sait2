from django.contrib import admin
from .models import Articles, Complaints
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ComplaintsResource(resources.ModelResource):
    class Meta:
        model = Complaints

class ComplaintsAdmin(ImportExportModelAdmin):
    resource_class = ComplaintsResource

class ArticlesResource(resources.ModelResource):
    class Meta:
        model = Articles

class ArticlesAdmin(ImportExportModelAdmin):
    resource_class = ArticlesResource

admin.site.register(Complaints, ComplaintsAdmin)
admin.site.register(Articles, ArticlesAdmin)

