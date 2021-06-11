from django import forms
import numpy as np


class Search_Form(forms.Form):
    search_term = forms.CharField(required=True)
    