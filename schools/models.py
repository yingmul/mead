from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField
from django.contrib.localflavor.us.models import USStateField


class School(models.Model):
    name = models.CharField(max_length=200)


class SchoolAddress(models.Model):
    school = models.ForeignKey(School, related_name="addresses")
    address = models.CharField('Address 1', max_length=100, )
    address2 = models.CharField('Address 2', max_length=100, blank=True, null=True)
    city = models.CharField('City', max_length=100)
    state = USStateField('State')
    postal_code = models.CharField('Zip Code', max_length=10, null=True)
    phone_number = PhoneNumberField('Phone Number')  # mobile_phone (optional)

    class Meta:
        verbose_name = 'Profile Address'
        verbose_name_plural = 'Profile Addresses'

    def __unicode__(self):
        return "Address for {0}".format(self.school.name)

