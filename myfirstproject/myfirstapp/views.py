from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .myform2 import *
# Create your views here.
def error_404_view(request,exception):
    return render(request,'404.html')

def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionabout(request):
    return HttpResponse('About Response')

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    mydict = {
        'name' : name,
        'age' : age
    }
    return JsonResponse(mydict)

def myfirstpage(request):
    return render(request,'index.html')

def mysecondpage(request):
    return render(request,'second.html')

def mythirdpage(request):
    var = 'Hello World'
    greetings = 'Hey, How you doin?'
    fruits = ['apple','banana','pineapple']
    num1, num2 = 3,5
    ans = num1 > num2
    #print(ans)
    mydict = {
        'var' : var,
        'msg' : greetings,
        'myfruits' : fruits,
        'num1' : num1,
        'num2' : num2,
        'ans'  : ans   
        }
    return render(request,'third.html',context = mydict)

def myimagepage(request):
    return render(request, 'imagepage.html')

def myimagepage2(request):
    return render(request, 'imagepage2.html')

def myimagepage3(request):
    return render(request, 'imagepage3.html')

def myimagepage4(request):
    return render(request, 'imagepage4.html')

def myimagepage5(request, imagename):
    imagename = str(imagename)
    imagename = imagename.lower()
    print(imagename)
    if imagename == 'django':
        var=True
    elif imagename == 'python':
        var = False
    mydict = {
        'var':var
    }
    return render(request, 'imagepage5.html',context=mydict)

def myform(request):
    return render(request, 'myform.html')

def submitmyform(request):
    mydict = {
        'var1' : request.POST['mytext'],
        'var2' : request.POST['mytextarea'],
        'method' : request.method
    }
    return JsonResponse(mydict)

def myform2(request):
    if request.method == "POST":
        form = Feedbackform(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            mydict = {
                'form': Feedbackform()
            }
            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag = True
                errormsg = 'Title should be capital'
                Errors.append(errormsg)
                 #mydict['error'] = True
                 #mydict['errormsg'] = 'Title should start with Capital'
                 #return render(request, 'myform2.html', context=mydict)
            import re
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if not re.search(regex,email):
                errorflag = True
                errormsg = 'Email is not valid'
                Errors.append(errormsg)
            #else:
            if errorflag != True:
                mydict['success'] = True
                mydict['successmsg'] = 'Form submitted'
            
            mydict['error'] = errorflag
            mydict['errors'] = Errors
            print(mydict)
            return render(request, 'myform2.html', context=mydict)
            #print(title)
            #print(subject)
            #var = str('Form submitted ' + str(request.method))
            #return HttpResponse(var)
        #else:
         #   mydict = {
          #  'form' : form
           # }
            #return render(request, 'myform2.html', context=mydict) 
    elif request.method == "GET":
        form = Feedbackform() #Feedbackform(None)
        mydict = {
            'form' : form
        }
        return render(request, 'myform2.html', context=mydict)