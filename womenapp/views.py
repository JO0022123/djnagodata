from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def  home(request):
    data=student.objects.all().values() 
    return render(request,'index.html',{"data":data})

def adddata(request):
    if request.method=="POST":
        rollno=request.POST.get('rollno')
        name=request.POST.get('name')
        age=request.POST.get('age')
        city=request.POST.get('city')
        data1=student(rollno=rollno,name=name,age=age,city=city)
        data1.save()
        return redirect('Home')
    return render(request,"crud/addform.html")

def delete(request,id):
    obj1=student.objects.get(id=id)
    obj1.delete()
    return redirect('Home')

def edit(request,id):
    obj1=student.objects.get(id=id)
    if request.method=="POST":
        rollno=request.POST.get('rollno')
        name=request.POST.get('name')
        age=request.POST.get('age')
        city=request.POST.get('city')
        obj1.rollno=rollno
        obj1.name=name
        obj1.age=age
        obj1.city=city
        obj1.save()
        return redirect('Home')
    return render(request,'crud/editform.html',{"obj1":obj1})

def about(request):
    info=Product.objects.all()
    return render(request,'about.html',{"info":info})