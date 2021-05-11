from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

class Home(View):
    def get(self, request):
        
        return render(request,'index.html',{})
    def post(self,request):
        if request.is_ajax and request.method == "POST":
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            return JsonResponse({"data" : {'name': name, 'email': email, 'subject':subject,'message':message}},status=200)

class Apply(View):
    def get(self,request):
        return render(request, 'pages/apply.html')