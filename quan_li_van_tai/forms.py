from django import forms

class CarForm(forms.Form):
    id= forms.IntegerField()
    name= forms.CharField(max_length=100)
    diemdi= forms.CharField(max_length=100)
    diemden= forms.CharField(max_length=100)
    date= forms.DateField()
    phone= forms.IntegerField()
    email= forms.CharField(max_length=100)
    address = forms.CharField(max_length=200),
    
class VexeForm(forms.Form):
    id= forms.IntegerField()
    diemdi= forms.CharField(max_length=100)
    diemden= forms.CharField(max_length=100)
    date= forms.DateField()
    giave= forms.FloatField()