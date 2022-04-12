from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import usersForm

def home(request):
    data={
        "title":"HOMEPAGE",
        "body":"hi mera name vikrant hai",
        "list":['python','django','c++'],
        "number":[4,5,6,7,8,9],
        'student_detail':[
            {"name":"Vikrant","contact":6394321843},
            {"name":"pradeep","contact":4178652234}
        ]
    }
    return render(request,"index.html",data)

def aboutUs(request):

    return render(request,"about.html")

def post(request):

    finalres=0

    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalres=n1+n2;
            data={
                'n1':n1,
                'n2':n2,
                'output':finalres
            }

            return HttpResponseRedirect('/about/')

    except:
        pass

    return render(request, "post.html",data)
def post(request):

    finalres=0

    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalres=n1+n2;

    except:
        pass

    return render(request, "post.html", {'output': finalres})



def teamMED(request):
    a = "<h1>The Names of MED Team Members are :</h1>"
    list = ["Param sir", "Mandy sir", "Akasha sir", "Pratiksha mam", "Vikrant sir"]
    for i in list:
        a = a + "<br><h3>" + i + "</h3>"
    return HttpResponse(a)


def form(request):
        finalans=0

        #title:"hi frends"
        try:
            #n1=int(request.GET['num1'])
            #n2=int(request.GET['num2'])
            n1=int(request.GET.get('num1'))
            n2=int(request.GET.get('num2'))
            finalans=n1+n2
        except:
            pass


        return render(request, "userform.html",{'output':finalans})

def submitform(request):
    fn = usersForm()
    data = {'form': fn}

    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalres=n1+n2;
            data={
                'form':fn,
                'output':finalres
            }

            return HttpResponse(finalres)

    except:
        pass

    return render(request,"userform.html",data)



def courses(request):
    return HttpResponse('''<h1>Vikrant</h1><a href https://www.youtube.com/watch?v=yDYsvnSBZFs&list=PLjVLYmrlmjGcyt3m6rt21nfjhYSWP_Ue_&index=15>Search More</a>''')

def coursedetail(request,courseid):
    return HttpResponse(courseid)
