from django.db import models
from django.contrib.postgres.fields import ArrayField

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
    isbn = models.CharField(max_length=20)  
    bname = models.CharField(max_length=100)  
    bdesc = models.TextField()
    bauthor = models.CharField(max_length=15)
    bissuedate = models.DateField()
    bissue = models.CharField(max_length=20)
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