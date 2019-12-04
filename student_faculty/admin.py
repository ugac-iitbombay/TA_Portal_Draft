from django.contrib import admin
from student_faculty.models import *

admin.site.register(StudentUser)
admin.site.register(FacultyUser)
admin.site.register(Course)
admin.site.register(Application)
admin.site.register(StudentFeedback)
admin.site.register(FacultyFeedback)

# Register your models here.
