from django import forms
from .models import MyUser


class StudentRegistrations(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ["name", "email", "password"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(
                render_value=True, attrs={"class": "form-control"}
            ),
        }
