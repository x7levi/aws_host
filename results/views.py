from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Student, Subject
from .forms import StudentForm, SubjectForm


def home(request):
    context = {}
    if request.method == 'POST':
        reg = request.POST.get('register_no', '').strip()
        if not reg:
            messages.error(request, 'Please enter a register number')
        else:
            try:
                student = Student.objects.get(register_no=reg)
                return redirect('results:view_result', register_no=student.register_no)
            except Student.DoesNotExist:
                messages.error(request, 'Register number not found')
    return render(request, 'results/home.html', context)


def view_result(request, register_no):
    student = get_object_or_404(Student, register_no=register_no)
    subjects = student.subjects.all()
    total = sum(s.marks for s in subjects)
    count = subjects.count()
    percentage = 0
    status = 'PASS'
    if count > 0:
        percentage = (total / (count * 100.0)) * 100.0
    # If any subject mark < 40 -> FAIL
    if any(s.marks < 40 for s in subjects):
        status = 'FAIL'
    context = {
        'student': student,
        'subjects': subjects,
        'total': total,
        'percentage': round(percentage, 2),
        'status': status,
    }
    return render(request, 'results/result.html', context)


@login_required
def dashboard(request):
    return render(request, 'results/dashboard.html')


@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Student added successfully')
            return redirect('results:student_list')
    else:
        form = StudentForm()
    return render(request, 'results/add_student.html', {'form': form})


@login_required
def add_subject(request, student_id=None):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject added')
            return redirect('results:student_list')
    else:
        initial = {}
        if student_id:
            initial['student'] = get_object_or_404(Student, id=student_id)
        form = SubjectForm(initial=initial)
    return render(request, 'results/add_subject.html', {'form': form})


@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'results/student_list.html', {'students': students})


@login_required
def edit_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject updated')
            return redirect('results:student_list')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'results/add_subject.html', {'form': form, 'edit': True})


@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    messages.success(request, 'Student deleted')
    return redirect('results:student_list')
