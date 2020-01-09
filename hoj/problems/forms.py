from ckeditor.fields import RichTextFormField

from django import forms
from submission.models import Submission

class SubmitForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('language', 'code')
