from django import forms
from .models import Student, Subject


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'register_no', 'course', 'semester']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['student', 'subject_name', 'marks']
