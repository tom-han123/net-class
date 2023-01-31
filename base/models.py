from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class account_registeration(models.Model):
    user_id = models.AutoField(db_column="User_ID", primary_key=True)
    mail = models.CharField(db_column="Email", max_length=50, unique=True, blank=False, null=False)
    password = models.CharField(db_column="Password", max_length=50, null=False, blank=False)

    def __str__(self):
        return str(self.student_id)

class address(models.Model):
    address_id = models.AutoField(db_column="Address ID", primary_key=True)
    city = models.CharField(db_column="City_Town", max_length=100, unique=True, blank=False)
    state_region = models.CharField(db_column="State_Region", max_length=100, blank=False)
    
    def __str__(self):
        return str(self.address_id)


class student(models.Model):
    student_id = models.ForeignKey(account_registeration, on_delete=models.CASCADE)
    first_name = models.CharField(db_column="First_Name", max_length=50, blank=True)
    last_name = models.CharField(db_column="Last_Name", max_length=50, blank=True)
    phone1 = models.CharField(max_length=15, null=False,blank=False,unique=True)
    phone2 = models.CharField(max_length=15, null=True,blank=True,unique=True)
    mail = models.EmailField(max_length=100,null=False, unique=True,blank=False)
    address_id = models.ForeignKey(address, on_delete=models.SET_NULL, null=True)
    classroom = models.JSONField()
    age = models.IntegerField(blank=False, null=False)
    gender = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return str(self.student_id)

class payforclass(models.Model):
    payment_Id = models.AutoField(db_column="Payment_Id", primary_key=True)
    classroom_id = models.ForeignKey(db_column="Classroom_Id", on_delete=models.CASCADE)
    student_id = models.ForeignKey(account_registeration, on_delete=models.CASCADE)
    approved = models.BooleanField(db_column="Isapproved")

    def __str__(self):
        return str(self.payment_Id) 
    

class teacher_registeration(models.Model):
    teacher_id = models.AutoField(db_column="Teacher ID", primary_key=True)
    mail = models.CharField(db_column="Email", max_length=50)
    password = models.CharField(db_column="Password", max_length=50, null=False, blank=False)
    approve = models.BooleanField(db_column="Isapproved")

    def __str__(self):
        return self.mail

    

class teacher(models.Model):
    teacher_id = models.ForeignKey( teacher_registeration,db_column="Teacher ID", primary_key=True)
    first_name = models.CharField(db_column="First_Name", max_length=50, blank=True)
    last_name = models.CharField(db_column="Last_Name", max_length=50, blank=True)
    phone1 = models.CharField(max_length=15, db_column="Personal Phone", null=False,blank=False,unique=True)
    phone2 = models.CharField(max_length=15, db_column="Emergency Phone", null=True,blank=True,unique=True)
    mail = models.EmailField(db_column="Mail", max_length=100,null=False, unique=True,blank=False)
    address_id = models.ForeignKey(address, on_delete=models.SET_NULL, null=True)
    classroom = models.JSONField()
    subjects = models.JSONField()
    social_media = models.JSONField()
    age = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.teacher_id)


class classroom(models.Model):
    classroom_id = models.AutoField(db_column="Room ID", primary_key=True)
    classroom_name = models.CharField(db_column="Room Name", max_length=100, blank=False, unique=False)
    subject_id = models.JSONField()
    start_date = models.DateField()
    end_date = models.DateField()
    class_time = models.CharField(max_length=10)
    student_count = models.IntegerField(db_column="Student_count")
    price = models.IntegerField(db_column="Price")

    def __str__(self):
        return str(self.classroom_id)



class room_std_teacher(models.Model):
    relation_id = models.AutoField(db_column="Relation_Id", primary_key=True)
    classroom_id = models.ForeignKey(classroom, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(teacher, on_delete=models.CASCADE)
    student_id = models.ForeignKey(account_registeration, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.relation_id)

class subject(models.Model):
    subject_id = models.AutoField(db_column="Subject_ID", primary_key=True)
    subject_name = models.CharField(db_column="Subject_Name", max_length=100, null=False, blank=False)

    def __str__(self):
        return str(self.subject_id)







    


