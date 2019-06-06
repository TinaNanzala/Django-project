from django.contrib import admin

# Register your models here.
from .models import Tutor

class TutorAdmin(admin.ModelAdmin):
	list_display =("staff_number","first_name","last_name","phone_number","email")
	search_fields =("staff_number","first_name","last_name")
admin.site.register(Tutor,TutorAdmin)
