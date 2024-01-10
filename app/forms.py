from django import forms
class Topicform(forms.Form):
    topic_name=forms.CharField()
class Webpageform(forms.Form):
    webpage_name=forms.CharField()
class Accessrecordform(forms.Form):
    Accessrecord_name=forms.CharField()
