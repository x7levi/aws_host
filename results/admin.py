from django.contrib import admin
from .models import Student, Subject


class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'register_no', 'course', 'semester')
    inlines = [SubjectInline]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'student', 'marks')
