from django.shortcuts import render
from Project.settings import EMAIL_HOST_USER
from django.views import View
from django.core.mail import send_mail
from core.models import *
from django.views.generic import ListView,DetailView

class Home(View):
    def get(self, request):
        return render(request,'index.html',{})
    def post(self,request):
        if request.method == "POST":
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
                document = request.FILES['file']
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            contact = request.POST.get('contact', '')
            send_mail("Vcodify Technologies",'''Thank's for submitting the form we appreciate you're decision to connect with us.''', EMAIL_HOST_USER, [email], fail_silently = False)
            application = Career(name=name,email=email,contact=contact,document=document)
            application.save()
            return render(request,'pages/apply.html',{"context":"message"})


class PortfolioView(ListView):
    model = Portfolio
    template_name = 'pages/portfolio.html'  
    context_object_name = 'pfdata'  
    paginate_by = 6
    queryset = Portfolio.objects.all().order_by('uploaded_at')

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'pages/portfolio_details.html'
    context_object_name = 'pfdata' 
     