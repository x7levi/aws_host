from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    register_no = models.CharField(max_length=50, unique=True)
    course = models.CharField(max_length=100)
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.register_no})"


class Subject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='subjects')
    subject_name = models.CharField(max_length=200)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.subject_name} - {self.marks}"
