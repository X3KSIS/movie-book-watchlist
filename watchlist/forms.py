from django import forms
from .models import WatchItem

class WatchItemForm(forms.ModelForm):
    class Meta:
        model = WatchItem
        fields = ['title', 'item_type', 'status', 'rating', 'review']
        widgets = {
            'review': forms.Textarea(attrs={'rows': 3}),
        }