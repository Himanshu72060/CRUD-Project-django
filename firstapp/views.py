from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistrations
from .models import MyUser

# Create your views here.


# This function will data add and show
def addshow(request):
    if request.method == "POST":
        fm = StudentRegistrations(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data["name"]
            em = fm.cleaned_data["email"]
            pw = fm.cleaned_data["password"]
            reg = MyUser(name=nm, email=em, password=pw)
            reg.save()
    else:
        fm = StudentRegistrations()
    stud = MyUser.objects.all()
    return render(request, "first/add_show.html", {"form": fm, "stu": stud})


# this will function update/edit
def update_data(request, id):
    if request.method == "POST":
        pi = MyUser.objects.get(pk=id)
        fm = StudentRegistrations(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = MyUser.objects.get(pk=id)
        fm = StudentRegistrations(instance=pi)
    return render(request, "first/updatestudent.html", {"form": fm})


# This function will data delete
def data_delete(request, id):
    if request.method == "POST":
        pi = MyUser.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect("/")
