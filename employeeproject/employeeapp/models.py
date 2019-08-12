from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Address(models.Model):
    street_no = models.CharField(max_length = 65)
    city = models.CharField(max_length = 65)
    state = models.CharField(max_length = 65)
    pincode = models.CharField(max_length = 65)
    country = models.CharField(max_length = 65)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    def __str__(self):
        return self.city


class Profile(models.Model):
    GENDER_CHOICES = (
      ('male', 'Male'),
      ('female', 'Female')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'usermodel')
    permanent_address_city = models.ForeignKey(Address,on_delete=models.CASCADE,related_name = 'permanent_address_city')
    phone_number = models.PositiveIntegerField()
    gender = models.CharField(max_length = 5,choices = GENDER_CHOICES)
    # profile_pic = models.ImageField(upload_to='profile_pic',default = 'default.jpg')
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
