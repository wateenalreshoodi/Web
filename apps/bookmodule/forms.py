from django import forms
from .models import Student, Address, ImageGallery

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'address']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'state', 'zip_code']

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageGallery
        fields = ['title', 'image']
