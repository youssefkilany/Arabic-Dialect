from django import forms

class DialectRecognizerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Wanna say something..?"
        })
    )
