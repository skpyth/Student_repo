from django.db import models



class Student(models.Model):
    fname = models.CharField('stud_fname',max_length=30)
    lname = models.CharField('stud_lname', max_length=30)
    email = models.EmailField('stud_email')
    dob = models.CharField('stud_dob', max_length=30)
    contact = models.BigIntegerField('stud_mob')
    qual = models.CharField('stud_qual', max_length=30)
    gender =models.CharField('stud_gen', max_length=30)
    active = models.CharField('active', max_length=30,default='Y')
    created = models.DateTimeField('created_date', auto_now_add=True)
    updated = models.DateTimeField('modified_date', auto_now=True)

    @staticmethod
    def get_empty_student():
        return Student(id=0,fname='',lname='',email='',dob='',qual='',contact=0,gender='')

    class Meta:
        db_table = 'Stud_Info'

class Courses(models.Model):
    name = models.CharField('cr_name', max_length=30)
    code = models.CharField('cr_code', max_length=30)
    fees = models.FloatField('cr_fee')
    duration = models.CharField('cr_duration', max_length=30)
    active = models.CharField('active', max_length=30,default='Y')
    created = models.DateTimeField('created_date',auto_now_add=True)
    updated = models.DateTimeField('modified_date',auto_now=True)

    studrefs = models.ManyToManyField(Student,related_name='courserefs')

    @staticmethod
    def get_empty_course():
        return Courses(id=0, name='', code='', fees=0.0, duration='')

    class Meta:
        db_table = 'Courses_Info'

