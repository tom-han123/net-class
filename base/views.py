from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import redirect, render
from django.contrib import messages
from .serializers import stdregserializer, studentserializer, addrserializer, teacherserializer, classroomserializer, roomstdtecserializer, subjectserializer
from .models import student_registeraiton, address, student, teacher, classroom, room_std_teacher, subject
def index(request):
    return HttpResponse('Hello World')


# def std_login_signup(request):
#     if request.method == 'POST':
#         try:
#             if 'register_form' in request.POST:
#                 phone = request.POST.get('email')
#                 password = request.POST.get('pass1')
#                 repass = request.POST.get('pass2')
#                 if password == repass:
#                     newacc = student_registeraiton.objects.create(phone=phone, password = password)
#                     newacc.save()
#                     messages.success(request, 'Create new account successful...')
#                 else: messages.info(request, 'The two passwords does not match each other...')
#             elif 'login_form' in request.POST:
#                 found = False
#                 phone = request.POST.get('phone')
#                 password = request.POST.get('pass')
#                 accs = student_registeraiton.objects.all().values()
#                 for acc in accs:
#                     if acc['phone'] == phone:
#                         if acc['password'] == password:
#                             found = True
#                             break
#                 if found:
#                     messages.success(request, 'Login successful...')
#                 else: messages.info(request, 'Your phone no or password is incorrect...')
                    
#         except Exception as e:
#             messages.info(request, e)
#     return render(request, 'base/login_signup.html')

