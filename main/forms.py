from django import forms
from .models import  Choice, Vote



class VoteForm(forms.ModelForm):
    choice = forms.ModelChoiceField(queryset=Choice.objects.none(), widget=forms.RadioSelect)

    class Meta:
        model = Vote
        fields = ['choice']

    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['choice'].queryset = question.choices.all()