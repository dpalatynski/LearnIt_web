from django import forms
from crispy_forms.helper import FormHelper
from .models import FlashcardCheckAnswer
from crispy_forms.layout import Layout, Row, Column, Field


class FlashcardCheckAnswerModelForm(forms.ModelForm):
    answer = forms.CharField(required=False, widget=forms.TextInput(attrs={'autofocus': True}))

    def __init__(self, *args, **kwargs):
        super(FlashcardCheckAnswerModelForm, self).__init__(*args, **kwargs)
        self.fields['answer'].label = ""
        self.fields['answer'].blank = True

    class Meta:
        model = FlashcardCheckAnswer
        fields = ['answer']

