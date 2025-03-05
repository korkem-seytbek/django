from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["name", "date", "user"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }

