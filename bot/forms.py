from django import forms
from django.shortcuts import render

class LyricForm(forms.Form):
    lyric = forms.CharField(required = True)
    lines = forms.IntegerField(required = True)
    def generate_lyric(self):
        pass
