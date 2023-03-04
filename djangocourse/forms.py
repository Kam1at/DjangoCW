from django import forms
from djangocourse.models import Client, Message, DistributionList


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['owner']


class DistributionForm(forms.ModelForm):
    class Meta:
        model = DistributionList
        exclude = ['owner']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['owner']
