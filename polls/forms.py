from django import forms
from polls.models import *
from dataclasses import fields

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'question_text',
            'pub_date'
        ]
