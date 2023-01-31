from rest_framework import serializers
from .models import account_registeration, address, student, teacher_registeration,teacher, classroom, room_std_teacher, subject, payforclass

class accregserializer(serializers.ModelSerializer):
    class Meta:
        model = account_registeration
        fields = "__all__"

class addrserializer(serializers.ModelSerializer):
    class Meta:
        model = address
        fields = "__all__"

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = "__all__"


class tecregserializer(serializers.ModelSerializer):
    class Meta:
        model = teacher_registeration
        fields = "__all__"

class teacherserializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = "__all__"


class classroomserializer(serializers.ModelSerializer):
    class Meta:
        model = classroom
        fields = "__all__"

class roomstdtecserializer(serializers.ModelSerializer):
    class Meta:
        model = room_std_teacher
        fields = "__all__"


class subjectserializer(serializers.ModelSerializer):
    class Meta:
        model = subject
        fields = "__all__"


class payserializer(serializers.ModelSerializer):
    class Meta:
        model = payforclass
        fields = "__all__"


