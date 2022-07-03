from django.contrib import admin
from .models import Student, Place, Projects, Lesson
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(Student)
class student(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Place)
class place(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Projects)
class projects(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Lesson)
class lesson(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

