from django.shortcuts import render
from Project.settings import EMAIL_HOST_USER
from django.views import View
from django.core.mail import send_mail
from core.models import *

class Home(View):
    def get(self, request):
        return render(request,'index.html',{})
    def post(self,request):
        if request.is_ajax and request.method == "POST":
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            send_mail("Vcodify Technologies",'''Thank's for submitting the data we will reached you as soon as possible.''', EMAIL_HOST_USER, [email], fail_silently = False)
            contact = Contact(name=name,email=email,subject=subject,message=message)
            contact.save()
            return render(request,'index.html',{"context":"message"})


class Apply(View):
    def get(self,request):
        return render(request, 'pages/apply.html')  
    def post(self,request):
        if request.method == "POST":
            if request.FILES :
                file = request.FILES['file']
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            contact = request.POST.get('contact', '')
            gender = request.POST["gender"]
            dob = request.POST['dob']
            address = request.POST['address']
            address2 = request.POST['address2']
            state = request.POST['state']
            city = request.POST['city']
            zipcode = request.POST['zip']
            send_mail("Vcodify Technologies",'''Thank's for submitting the form we appreciate you're decision to connect with us.''', EMAIL_HOST_USER, [email], fail_silently = False)
            # application = Career(name=name,email=email,subject=subject,message=message)
            # application.save()
            return render(request,'pages/apply.html',{"context":"message"})