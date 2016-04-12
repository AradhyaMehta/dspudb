from django.contrib import admin

from .models import University
from .models import Department
from .models import Student
from .models import Employee

# Register your models here.
admin.site.site_header = 'University Information Database'
#admin.site.
admin.site.register(University)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Employee)
