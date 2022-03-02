from cProfile import label
from django import forms
from crud_trainer.models import Trainer

class TrainerForm(forms.ModelForm):
    
    class Meta:
        model = Trainer
        fields = ('first_name', 'last_name', 'subject')
        labels = {
            'first_name':'Full Name',
            'last_name':'Last Name',
            'subject':'Subject'
        }
