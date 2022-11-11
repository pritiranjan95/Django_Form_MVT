from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect
from name.models import Form
from django.http import HttpRequest
# Create your views here.


def index(request):
    return HttpResponse("Hi this is a blank page as your url is only th eserver name")

#To show the html page directly
def contact(request):
    return render(request, "contact.html")

#For a template
def home(request):
    data={"Name": "Bapiiiiiiiiiiiiiiiiiiiiiiiiiiii",
    "skill":["Python", "Digital Marketing", "PHP"],
    "age":{"no":[23,33,44,55,66]}}

    return render(request, "hey.html",data)

# def detail(request):
#     a=request.GET.get("name of the form input")
#     b=request.GET.get("Name of form input2")
#     c=request.POST.get()
#     return render(request,"hey.html")

def about(request):
    return HttpResponsePermanentRedirect("/contact") #it will redirect the about--us page to contact page
    
#Saving data for model by considering the form page given names. -----POST METHOD-----
def form(request):
    if request.method=="POST":
        first_name=request.POST.get("fname")
        last_name=request.POST.get("lname")
        a= Form(First_name=first_name, Last_name=last_name)
        a.save()   #It will automatically save the data in my database
        
    return render(request, "form.html")


#For Thank you page
def thanks(request):
    return render(request, "thank.html")
