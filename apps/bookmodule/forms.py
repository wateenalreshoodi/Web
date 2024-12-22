from django import forms
from .models import Book, Address, Student, Address2, Student2, ImageModel

# ---------------------------
# Book Form
# ---------------------------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']


# ---------------------------
# Address Form
# ---------------------------
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']


# ---------------------------
# Student Form (Many-to-Many with Addresses)
# ---------------------------
class StudentForm(forms.ModelForm):
    addresses = forms.ModelMultipleChoiceField(
        queryset=Address.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Student
        fields = ['name', 'age', 'addresses']


# ---------------------------
# Address2 Form
# ---------------------------
class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['city']


# ---------------------------
# Student2 Form (Many-to-Many with Addresses2)
# ---------------------------
class Student2Form(forms.ModelForm):
    addresses = forms.ModelMultipleChoiceField(
        queryset=Address2.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']


# ---------------------------
# Image Upload Form
# ---------------------------
class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['title', 'image']
