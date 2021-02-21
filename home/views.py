from django.shortcuts import render, redirect
from .models import  short_urls
from .forms import UrlForm
from .shortner import shortner
# Create your views here.

def index(request):
    form = UrlForm(request.POST)
    a = ''
    l=''
    if request.method == "POST":
        if form.is_valid():
            temp = form.cleaned_data['long_url']
            print("temppp", temp)
            obj = short_urls.objects.filter(long_url=temp)
            if obj:               #if long url is alredy in database then we will query it and get short_url
                a = obj[0].short_url
                return render(request, 'index.html', {'form':form , 'a':a})
                
            NewUrl = form.save(commit=False)
            mc = shortner()
            a = mc.issue_token()
            print('------------------------', a )
            NewUrl.short_url = a
            NewUrl.save()
        else:
            
            form = UrlForm()
            a = "Invalid URL"
            '''
            name = form.cleaned_data['username']
            '''
           
    else:
        form = UrlForm()

    return render(request, 'index.html', {'form':form , 'a':a})


def original(request, token):
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)
