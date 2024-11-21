from django.shortcuts import render
from .models import StudentsData
def mainPage(request):
        data = StudentsData.objects.all()
        return render(request, 'mainpage.html', {'data':data})


def add_student(request):
    if request.method == 'GET':
        data = StudentsData.objects.all()
        return render(request, 'add_student.html')
    else:
        fname1 = request.POST.get('fname')
        lname1 = request.POST.get('lname')
        email1 = request.POST.get('email')
        mobile1 = request.POST.get('mobile')
        percentage1 = request.POST.get('percentage')
        year1 = request.POST.get('year')
        location1 = request.POST.get('location')
        college1 = request.POST.get('college')
        university1 = request.POST.get('university')
        StudentsData(
            first_name = fname1,
            last_name = lname1,
            email = email1,
            mobile = mobile1,
            percentage = percentage1,
            year = year1,
            location = location1,
            college_name = college1,
            university = university1
        ).save()
        data = StudentsData.objects.all()
        return render(request, 'mainPage.html', {'data':data})
