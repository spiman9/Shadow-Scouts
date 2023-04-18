from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"homepage.html")

def contact(request):
    return render(request,"contactUs.html")

def about(request):
    return render(request,"about.html")

def profile(request):
    return render(request,"profile.html")

def leave(request):
    return render(request,"leave.html")