from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField
from django.contrib.localflavor.us.models import USStateField


class School(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class SchoolAddress(models.Model):
    school = models.ForeignKey(School, related_name="addresses")
    address = models.CharField('Address 1', max_length=100, )
    address2 = models.CharField('Address 2', max_length=100, blank=True, null=True)
    city = models.CharField('City', max_length=100)
    state = USStateField('State')
    postal_code = models.CharField('Zip Code', max_length=10, null=True)
    phone_number = PhoneNumberField('Phone Number', blank=True, null=True)  # mobile_phone (optional)

    class Meta:
        verbose_name = 'School Address'
        verbose_name_plural = 'School Addresses'

    def __unicode__(self):
        return "Address for {0}".format(self.school.name)


class Class(models.Model):
    school = models.ForeignKey(School, related_name='classes')
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    # TODO: add status: open, wait list, only 2 left

    class Meta:
        verbose_name_plural = 'Classes'

    def __unicode__(self):
        return "Class {0} for {1}".format(self.name, self.school.name)


class Schedule(models.Model):
    school_class = models.ForeignKey(Class, related_name="class_schedules")
    start_date = models.DateField('Start Date')
    num_meetings = models.IntegerField(default=1)
    start_time = models.TimeField('Start Time')
    end_time = models.TimeField('End Time')
    max_students = models.IntegerField(null=True)

    def __unicode__(self):
        return 'Schedule {0} for {1}'.format(self.start_date, self.school_class.name)


class Instructor(models.Model):
    schedule = models.ForeignKey(Schedule, related_name="instructors")
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, default='')
    website = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name