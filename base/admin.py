from django.contrib import admin
from .models import account_registeration, student,  teacher_registeration,teacher, address, classroom, room_std_teacher, subject, payforclass

# Register your models here.

admin.site.register(account_registeration)
admin.site.register(student)
admin.site.register(teacher_registeration)
admin.site.register(teacher)
admin.site.register(address)
admin.site.register(classroom)
admin.site.register(room_std_teacher)
admin.site.register(subject)
admin.site.register(payforclass)
