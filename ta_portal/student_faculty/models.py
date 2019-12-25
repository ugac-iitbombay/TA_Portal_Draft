from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import date,datetime,timedelta
from student_faculty.choices import *
from uuid import uuid4
from django.contrib.auth.models import User
'''
class MyUser(AbstractUser):
	username = models.CharField(('username'), max_length=30, unique = True)
	email = models.EmailField(('email address'),blank=True)
	first_name =  models.CharField(('First name'),max_length=30,blank = True)
	last_name = models.CharField(('Last name'),max_length=30,blank = True)

	USERNAME_FIELD = 'username'
'''
class StudentUser(models.Model):
# add additional fields in here
    class Meta:
    	db_table="Student Users"


    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(User, related_name='student_user', on_delete=models.CASCADE, null=True, blank=True)
    ldap_id = models.CharField(max_length=50, null=True, blank=True)
    roll_no=models.CharField(('Roll Number'),max_length=9,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    year_of_study=models.CharField(('Year Of Study'),max_length=1,null=True, blank=True)
    contact_no=models.CharField(('Phone'),max_length=12,null=True, blank=True)
    cpi=models.FloatField(('CPI'),null=True, blank=True)
    selected_yet=models.BooleanField(default=False,null=True, blank=True)

    department = models.CharField(max_length=30, null=True, blank=True)
    department_name = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    degree_name = models.CharField(max_length=200, null=True, blank=True)
    join_year = models.CharField(max_length=5, null=True, blank=True)
    graduation_year = models.CharField(max_length=5, null=True, blank=True)
    def __str__(self):
    	return self.user.username
'''
    def save(self, *args, **kwargs):
    	self.cpi = round(self.cpi, 2)
    	super(StudentUser, self).save(*args, **kwargs)
'''

	
def contact_default():
    return {"firstname": "Web",
            "lastname":"Nominee"}


class FacultyUser(models.Model):
# add additional fields in here


	class Meta:
		db_table="Faculty Users"
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, null=True, blank=True)
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	ldap_id = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
	department = models.CharField(max_length=30, null=True, blank=True)
	department_name = models.CharField(max_length=200, null=True, blank=True)	#contact_no=models.CharField(('Phone'),max_length=12)
	def __str__(self):
		return self.user.username

class Course(models.Model):
	#id created by defualt
	class Meta:
		unique_together=(('course_name','year','semester'),)

	course_name=models.CharField(('Course Name'),max_length=40)
	profs=models.ManyToManyField(FacultyUser)
	course_details=models.CharField(('Course Details'),max_length=1000,blank=True)
	eligibility_criteria=models.CharField(('Eligibility'),max_length=500,blank=True)
	department = models.CharField(max_length=30, null=True, blank=True)
	department_name = models.CharField(max_length=200, null=True, blank=True)
	deadline=models.DateField(default=date.today()+timedelta(days=7),blank=False,)
	duration=models.CharField(default='Full Semester',choices=DURATION_CHOICES,max_length=20)
	extra_questions=models.CharField(max_length=1500)
	year=models.IntegerField(blank=False)
	semester=models.PositiveSmallIntegerField(blank=False,choices=SEM_OPTIONS)
	pass

class Application(models.Model):
	course=models.ForeignKey(Course,on_delete=models.CASCADE)
	student=models.ForeignKey(StudentUser,on_delete=models.CASCADE)
	status=models.CharField(max_length=100,choices=STUDENT_STATUS,default='On Hold')
	grade=models.CharField(('Grade'),max_length=2)
	answers_to_questions=models.CharField(('Answers'),max_length=6000)
	# to be used only is status is waitlist
	waitlist_num=models.IntegerField(('Waitlist Number'))
	created_or_modified=models.DateTimeField(('Last Modified'),auto_now=True)

	pass

#This will store the 
class StudentFeedback(models.Model):

	course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='student_feedback_course')
	student=models.ForeignKey(StudentUser,on_delete=models.CASCADE,related_name='student_feedback_student')
	#replace field with actual attributes to put
	field1=models.IntegerField(('Field1- Replace with actual parameter'),choices=RATINGS)
	field2=models.IntegerField(('Field2'),choices=RATINGS)
	field3=models.IntegerField(('Field3'),choices=RATINGS)
	comments=models.CharField(('Comments'),max_length=1000)

