from django import forms
from .models import TeamDetail


class TeamDetailForm(forms.ModelForm):

    class Meta:
        model = TeamDetail
        fields = "__all__"