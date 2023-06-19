from django.shortcuts import render,redirect 
from .models import Student
from django.contrib import messages

# Create your views here.
def index(request):
    data=Student.objects.all() #all data store in this 
    context={"data":data}
    return render(request,"index.html",context)


def insertData(request):    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()
        messages.info(request,"Data Inserted successfully")
        return redirect("/")

    return render(request,"index.html")

def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']

        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.gender=gender
        edit.save()
        messages.warning(request,"Data Updated successfully")
        return redirect("/")
    d=Student.objects.get(id=id) #all data store in this 
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=Student.objects.get(id=id) #all data store in this 
    d.delete()
    messages.error(request,"Data deleted successfully")
    return redirect("/")

def about(request):
    return render(request,"about.html")



