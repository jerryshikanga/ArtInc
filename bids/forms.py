from django import forms
from .models import Bid

class NewBidForm(forms.ModelForm):
    class Meta:
        """docstring for Meta."""
        model = Bid
        fields = ['amount']
