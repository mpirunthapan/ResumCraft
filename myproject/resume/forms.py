from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "name",
            "email",
            "phone",
            "linkedin",
            "github",
            "portfolio",
            "role",
            "summary",
            "degree",
            "university",
            "experience",
            "skills",
            "projects",
        ]

        widgets = {
            "summary": forms.Textarea(attrs={"rows": 4}),
            "experience": forms.Textarea(attrs={"rows": 4}),
            "skills": forms.Textarea(attrs={"rows": 3}),
            "projects": forms.Textarea(attrs={"rows": 4}),
        }
