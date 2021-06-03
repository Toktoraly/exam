from django.db.models import fields
from django.forms import ModelForm
from .models import Massage

class MassageForm(ModelForm):
    class Meta:
        model = Massage
        fields = "__all__"
