from django import forms

from .models import ShopTipModel, RecordedTask

class AddForm(forms.ModelForm):
    class Meta:
        model = ShopTipModel
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '品物'}),
        }

class RecordedForm(forms.ModelForm):
    class Meta:
        model = RecordedTask
        fields = ('title', 'memo', )