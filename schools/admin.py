from schools.models import School, Class, SchoolAddress, Schedule, Instructor
from django.contrib import admin

class AddressInline(admin.StackedInline):
    model = SchoolAddress
    extra = 1


class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 1


class InstructorInline(admin.StackedInline):
    model = Instructor
    extra = 1


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')


class SchoolAdmin(admin.ModelAdmin):
    inlines = [AddressInline]
    list_display = ('name', 'website')


class ClassAdmin(admin.ModelAdmin):
    inlines = [ScheduleInline]
    list_display = ('school', 'name', 'price')


admin.site.register(School, SchoolAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Instructor, InstructorAdmin)