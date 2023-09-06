from django import forms
from template_app.models import Tweet
from django.forms import ModelForm

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label="Nickname",max_length=50)
    message_imput = forms.CharField(label="message",max_length=100,
                                    widget=forms.Textarea(attrs={"class":"tweetmessage"}))
    
class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields =["username","message"]