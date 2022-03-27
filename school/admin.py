
from django.contrib import admin
from .models import Student,City_master,State_master

# Register your models here.
admin.site.register(Student)
admin.site.register(State_master)
admin.site.register(City_master)