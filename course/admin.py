from django.contrib import admin

# Register your models here.
from .models import Course


class CourseAdmin(admin.ModelAdmin):
	list_display =("name","duration_in_months")
	search_fields =("name","tutor__first_name","duration_in_months",)
admin.site.register(Course,CourseAdmin)