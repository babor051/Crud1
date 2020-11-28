from django.shortcuts import render
from .models import User
from .forms import StudentForm
from django.http import JsonResponse

# Create your views here.

def home(request):
    form = StudentForm()
    users = User.objects.all()

    context = {'form':form, 'users':users}
    
    return render(request, 'home.html', context)


def saveData(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if (sid == ''):
                user = User(name=name, email=email, password=password)
            else:
                user = User(id=sid, name=name, email=email, password=password)
            user.save()

            std = User.objects.values()
            student_data = list(std)
            return JsonResponse({'status': 'save', 'student_data': student_data})
        else:
            return JsonResponse({'status': 0})


def deleteData(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        print(id)
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def editData(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        std = User.objects.get(pk=id)
        student_data = {'id':std.id, 'name':std.name, 'email':std.email, 'password':std.password}
        return JsonResponse(student_data)
