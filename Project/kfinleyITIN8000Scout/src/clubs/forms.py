"""
------------------------------------------------------------
This creates the forms for "create".

Fields displayed are in the Meta class
            'title',
            'description',
            'person_in_charge',
            'meeting_info',
            'club_keywords',

Display details and input constraints are placed into ClubForm
and RawCLubForm classes. clubs/models.py is where the database
details are located.

* RawCLubForm is not used at the moment
------------------------------------------------------------
check out https://docs.djangoproject.com/en/3.2/ref/forms/fields/
for django form fields documentation
------------------------------------------------------------
"""
from django import forms
from .models import Club
# ------------------------------------------------------------
# ------------------------------------------------------------
class ClubForm(forms.ModelForm):
    title       = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    person_in_charge       = forms.CharField(label='',
                    widget=forms.TextInput(attrs={"placeholder": "Email of person in charge"}))
    meeting_info = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Where and when meeting happens",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 10,
                                    'cols': 120
                                }
                            )
                        )
    club_keywords       = forms.CharField(label='',
                    widget=forms.TextInput(attrs={"placeholder": "Keywords"}))

# ------------------------------------------------------------
# ------------------------------------------------------------
    class Meta:
        model = Club
        fields = [
            'title',
            'description',
            'person_in_charge',
            'meeting_info',
            'club_keywords',
        ]

# ------------------------------------------------------------
# ------------------------------------------------------------

class RawClubForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    person_in_charge       = forms.CharField(label='',
                    widget=forms.TextInput(attrs={"placeholder": "Email of person in charge"}))
    meeting_info = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Where and when meeting happens",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 10,
                                    'cols': 120
                                }
                            )
                        )
    club_keywords       = forms.CharField(label='',
                    widget=forms.TextInput(attrs={"placeholder": "Keywords"}))