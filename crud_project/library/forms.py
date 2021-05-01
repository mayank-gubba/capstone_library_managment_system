from django import forms  
from library.models import Book  
from django.forms import NumberInput

# LOCATION_CHOICES = [
#     ('MG_ROAD', 'MG Road'),
#     ('Karkhana', 'Karkhana'),
#     ('Hitech_City', 'Hi-Tech City'),
# ]

# ISSUE_CHOICES = [
#     ('available', 'Available'),
#     ('issued', 'Issued'),
#     ('ordered', 'Order Places'),
# ]


class BookForm(forms.ModelForm):  
    LOCATION_CHOICES = [
    ('MG_ROAD', 'MG Road'),
    ('Karkhana', 'Karkhana'),
    ('Hitech_City', 'Hi-Tech City'),
    ]
    ISSUE_CHOICES = [
    ('available', 'Available'),
    ('issued', 'Issued'),
    ('ordered', 'Order Places'),
    ]
    location = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=LOCATION_CHOICES)
    bissuedate = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    bissue = forms.ChoiceField(widget=forms.RadioSelect, choices=ISSUE_CHOICES)
    class Meta:  
        model = Book  
        fields = "__all__"  