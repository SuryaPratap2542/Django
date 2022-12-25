from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

def homePage(request):
    # This is for Practice file
    # data={
    #     "title":"welcome to Home Page" ,
    #     "bdata":"Welcome to my You tube channel Dream point",
    #     "clist":["PHP","Java","Python","CSS"],
    #     "numbers":[23,45,16,76,23,12,13,45,67,89,36],
    #     "num":[],
    #     "student_details":[
    #         {"name":"Ram","Phone":25823496},
    #         {"name":"Surya","Phone":324524678}
    #     ]
    # }
    # return render(request,"index.html",data)
    return render(request,"index.html")
def blog(request):
    return render(request,"blog.html")
def about(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"about.html",{'output':output})
def cart(request):
    return render(request,"cart.html")
def contact(request):
    return render(request,"contact.html")
def shop(request):
    return render(request,"shop.html")
def sproduct(request):
    return render(request,"sproduct.html")

def userform(request):
    data={}
    try:
        if request.method=="POST":
            n1=request.POST['num1']
            print(n1)
            n2=request.POST['num2']
            print(n2)
            n3=request.POST.get('num3')
            print(n3)
            n4=request.POST.get('num4')
            print(n4)
            data={
                "n1":n1,
                "n2":n2,
                "n3":n3,
                "n4":n4,
            }
            url="/about/?output={}".format(n1)
            return redirect(url)

    except:
        pass
    return render(request,"userform.html",data)
# def ind0(request):
#     return HttpResponse("Hello, world.<b> You're at the polls </b> index.")
# def ind1(request):
#     return HttpResponse("Hello, world.<b> You're at second index </b> index.")
# def ind2(request):
#     return HttpResponse("Hello, world.<b> You're at third  index </b> index.") 
# def courseDetails(request,courseid):
#     return HttpResponse(courseid)