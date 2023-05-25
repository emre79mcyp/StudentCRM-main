from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Student, Document

# Register your models here.
"""
This code defines the admin interface for the "Student" model in Django using the admin.ModelAdmin class. It also includes the ImportExportModelAdmin class, which suggests that the admin interface allows importing and exporting data for the "Student" model.

The list_display attribute specifies the fields to be displayed in the list view of the admin interface for each student. In this case, it includes the fields "id", "name", "passport_number", "nationality", "department", and "status". The list_display_links attribute specifies which fields should be linked to the detail view of the student when clicked. In this case, only the "name" field is linked.

The search_fields attribute specifies the fields that can be searched in the admin interface. In this case, searching can be performed based on the "first_name", "last_name", "student_id", and "passport_number" fields.

The inlines attribute is used to specify related models that can be edited inline with the parent model. In this case, the DocumentInline class is defined as an inline model admin for the "Document" model. It allows adding, editing, and deleting instances of the "Document" model directly from the admin interface of the "Student" model. The extra attribute is set to 1, which means one additional empty form for adding a document will be displayed by default.

The @admin.register(Student) decorator is used to register the "Student" model with the admin site and associate it with the StudentAdmin class defined above. This makes the admin interface accessible for managing student data.
"""


class DocumentInline(admin.StackedInline):
    model = Document
    extra = 1


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [DocumentInline]
    list_display = (
        "id",
        "name",
        "passport_number",
        "nationality",
        "department",
        "status",
    )
    search_fields = (
        "first_name",
        "last_name",
        "student_id",
        "passport_number",
    )
    list_display_links = ("name",)
