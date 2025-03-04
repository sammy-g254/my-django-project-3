from django.shortcuts import redirect, render
from .forms import StudentForm, RegisterForm
from .models import Student

# Create your views here.

#proj=create,read,update,delete
#list all students
def student_list(request):
    students=Student.objects.all()
    return render(request,'index.html',{'students':students})
#create a new student
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
def delete_student(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('index')
#update an existing student
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
            form.save()
            return redirect('index')
    return render(request,'register.html',{'form':form})