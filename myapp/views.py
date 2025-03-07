from django.shortcuts import redirect, render
from django.shortcuts import redirect
from .forms import StudentForm, RegisterForm
from .models import Student
from django.contrib.auth import login, logout
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

#proj=create,read,update,delete
#list all students
@login_required
def student_list(request):
    students=Student.objects.all()
    return render(request,'index.html',{'students':students})
#create a new student
@login_required
def create_student(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=StudentForm()      
    return render(request,'student_form.html',{'form':form})
#delete an old student
@login_required
def delete_student(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('index')
#update an existing student
@login_required
def update_student(request,id):
    student=Student.objects.get(id=id)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=StudentForm(instance=student)
    return render(request, 'student_form.html', {'form':form})
def register_user(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('index')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})
def login_user(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('index')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})
def logout_user(request):
    logout(request)
    return redirect('login')
