from django.shortcuts import render
from Dapp.models import Post
# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        ins=Post(name=name,email=email,message=message)
        ins.save()
    return render(request,"index.html")
