from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        "title":"welcome to Home Page" ,
        "bdata":"Welcome to my You tube channel Dream point",
        "clist":["PHP","Java","Python","CSS"],
        "numbers":[23,45,16,76,23,12,13,45,67,89,36],
        "num":[],
        "student_details":[
            {"name":"Ram","Phone":25823496},
            {"name":"Surya","Phone":324524678}
        ]
    }
    return render(request,"index.html",data)
def ind0(request):
    return HttpResponse("Hello, world.<b> You're at the polls </b> index.")
def ind1(request):
    return HttpResponse("Hello, world.<b> You're at second index </b> index.")
def ind2(request):
    return HttpResponse("Hello, world.<b> You're at third  index </b> index.") 
def courseDetails(request,courseid):
    return HttpResponse(courseid)