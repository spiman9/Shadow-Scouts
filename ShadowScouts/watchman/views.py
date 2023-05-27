from django.shortcuts import render , redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User , auth
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"homepage.html")

def contact(request):
    if(request.method == "POST"):
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['message']
        new_contact = Contact(name = name , email = email , message = msg)
        new_contact.save()

        # send email
        subject = 'Form submission Email'
        message = f'Successfully submitted the form'
        from_email = 'developers202304@gmail.com'  # replace with your email
        recipient_list = [email] # replace with recipient email(s)
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        
        recipient_list = ['developers202304@gmail.com']
        subject = f"Shadow Scouts: {name} wants to Connect"
        message = f"{name} has following message for you\n{msg}"
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        messages.success(request , 'Successfully Submitted the form')
        return render(request,"homepage.html")
    return render(request,"contactUs.html")

def about(request):
    return render(request,"about.html")

def profile(request):
    return render(request,"profile.html")

def leave(request):
    return render(request,"leave.html")

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['uname'] , password = request.POST['password'])
        if user is not None:
            auth.login(request , user)
            print("Loogin")
            # messages.success(request, "Successfully Login!!! " , {request.user}) 
            return redirect("/")
    return render(request , "login.html")

def register(request):
    if(request.method == "POST"):
        print(request.POST)
        return redirect("/")
    return render(request , "register.html")