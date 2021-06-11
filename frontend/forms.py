from django import forms


class Search_Form(forms.Form):
    search_term = forms.CharField(required=True)
    min_month = forms.IntegerField()
    max_month = forms.IntegerField()