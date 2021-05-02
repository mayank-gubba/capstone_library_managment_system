from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator

# PUBLISHER_CHOICE = (
#     ("McGraw_hill","McGraw Hill"),
#     ("Westland","Westland"),
#     ("Macmillan","Macmillan"),
# )
# Create your models here.
class Book(models.Model):  
    PUBLISHER_CHOICE = (
    ("McGraw_hill","McGraw Hill"),
    ("Westland","Westland"),
    ("Macmillan","Macmillan"),
    )
    isbn = models.PositiveBigIntegerField(validators=[MinValueValidator(1000000000000),MaxValueValidator(9999999999999)])  
    bname = models.CharField(max_length=100)  
    bdesc = models.TextField()
    bauthor = models.CharField(max_length=15)
    bprice = models.FloatField(validators=[MinValueValidator(0.00)],null=True)
    bissuedate = models.DateField(null=True)
    bissue = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images',null=True)
    location= ArrayField(
        models.CharField(max_length=40, blank=True),
        size=3, null=True
    )
    publisher = models.CharField(
        max_length = 20,
        choices = PUBLISHER_CHOICE,
        default = '1'
        )
    class Meta:  
        db_table = "book"