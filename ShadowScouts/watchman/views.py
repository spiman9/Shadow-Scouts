from django.shortcuts import render , redirect
from .models import Contact, Profile
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
            return redirect("/")
    return render(request , "login.html")

def register(request):
    if(request.method == "POST"):
        # print(request.POST)
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        # print(first_name  , pwd , last_name)
        pwd = request.POST.get("p")
        if request.POST.get("p") != request.POST.get("cp"):
            return render(request , "register.html")
        # render(request , "register_more_info.html" , {
        #     fname: first_name,
        #     lname : last_name,
        #     password : pwd
        # })
        # data = {
        #     'fname': first_name,
        #     'lname' : last_name,
        #     'password' : pwd
        # }

        # create usename here
        uname ="watchman_" + first_name[:4] + last_name[:4]

        request.session['registration_data'] = {
            'fname': first_name,
            'lname': last_name,
            'password': pwd,
            'uname' : uname,
        }

        return redirect("/register_main")
    return render(request , "register.html")


def register_main(request):
    data = request.session.get('registration_data', {})
    # This we got from sessions
    first_name = data.get('fname')
    last_name = data.get('lname')
    password = data.get('password')
    uname = data.get('uname')
    print(uname)


    if(request.method == "POST"):
        print("inside the post method of the register_main")
        # got from the submitted form
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        adharnumber = request.POST.get('adharnumber')
        phoneno = request.POST.get('pno')
       
    #    here only  user we have saved
        u = User.objects.create_user(username = uname , first_name=first_name , last_name = last_name , password=password)
        u.save()

        # here going to save for the Profile
        user_info = Profile()
        user_info.u_name = uname
        user_info.email = email
        user_info.aadhar_number = adharnumber
        user_info.phone_number = phoneno
        user_info.gender = gender
        user_info.full_name = first_name + " " + last_name
        
        user_info.save()
        # redirecting to the login page
        return redirect("/login")
    return render(request , "register_more_info.html" ,{'username' : uname})


def logoutuser(request):
    auth.logout(request)
    messages.success(request, "Logout Succesfully!!! " ) 
    return redirect("/")