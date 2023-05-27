from django import forms

class Feedbackform(forms.Form):
    title = forms.CharField(label='Title', max_length= 50, widget= forms.TextInput(attrs= {'class' : 'form-control'}))
    subject = forms.CharField(label= 'Subject Description', max_length=200, widget= forms.Textarea(attrs= {'class' : 'form-control'}))
    email = forms.CharField(label= 'Email', max_length=20, widget= forms.Textarea(attrs= {'class' : 'form-control'}))