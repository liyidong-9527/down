from django.forms.models import ModelForm
from .models import Resource


class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = "__all__"
