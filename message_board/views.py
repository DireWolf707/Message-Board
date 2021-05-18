from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse


def PostView(request):
    if request.method == 'POST':
        obj = Post(text=request.POST['message'])
        obj.save()
        return HttpResponseRedirect(reverse('home'))
    messages = Post.objects.all()
    return render(request,'home.html',{'messages':messages})