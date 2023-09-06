from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from . import models
from template_app.forms import AddTweetForm, AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


# Create your views here.
def index(request):
    return render(request,"template_app/first.html")

def weather_view(request):
    weather_dic={"istanbul": "30", "amsterdam" : "20",
                "paris":[10,20,30,40]
                 }
    return render(request,"template_app/weather.html",context=weather_dic)

def database(request):
    musician_data=models.Musician.objects.all().values()
    data_view={"musicians":musician_data}
    return render(request,"template_app/index.html",context=data_view)

def listtweet(request):
    tweets_data=models.Tweet.objects.all()
    tweet_dict={"tweets":tweets_data}
    return render(request,"template_app/listtweet.html",context=tweet_dict)

@login_required(login_url="/login")
def addtweet(request):
    if request.POST:
        message= request.POST["message"]
        models.Tweet.objects.create(username=request.user,message=message)
        #tweet = models.Tweet(nickname,message)
        #tweet.save()
        return redirect(reverse('template_app:listtweet'))
    else:
        return render(request,"template_app/addtweet.html")
    
def addtweetbyform(request):
    if request.POST:
        form=AddTweetForm(request.POST)
        if form.is_valid():
            nickname= request.POST["nickname_input"]
            message= request.POST["message_imput"]
            models.Tweet.objects.create(nickname=nickname,message=message)
            return redirect(reverse('template_app:listtweet'))
        else:
            print("error is form")
            return render(request,'template_app/addtweetbyform.html',context={"form":form})
    else:
        form=AddTweetForm()
        return render(request,'template_app/addtweetbyform.html',context={"form":form})
    
def addtweetbymodelform(request):
    if request.POST:
        form=AddTweetModelForm(request.POST)
        if form.is_valid():
           nickname= request.POST["nickname"]
           message= request.POST["message"]
           models.Tweet.objects.create(nickname=nickname,message=message)
           return redirect(reverse('template_app:listtweet'))
        else:
            print("error is form")
            return render(request,'template_app/addtweetbymodelform.html',context={"form":form})
    else:
        form=AddTweetModelForm()
        return render(request,'template_app/addtweetbymodelform.html',context={"form":form})
@login_required
def deletetweet(request,id):
    tweet =models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect('template_app:listtweet')
    



class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name= "registration/register.html"