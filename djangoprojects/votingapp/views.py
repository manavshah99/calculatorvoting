from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
arr = ['Java','Python','C++','C','DotNet','JavaScript','PHP','Swift','SQL','Ruby','R']
globalcnt = dict()
def index(request):
    mydict = {
        'arr':arr
    }
    return render(request,'index.html',context=mydict)

def getquery(request):
    q = request.GET['languages']
    if q in globalcnt:
        #if already exist then increment the value
        globalcnt[q] = globalcnt[q]+1
    else:
        #firsticcurence
        globalcnt[q] = 1
    mydict = {
        'arr':arr,
        'globalcnt': globalcnt
    }
    return render(request,'index.html',context=mydict)

def sortdata(request):
    global globalcnt
    globalcnt = (dict(sorted(globalcnt.items(),key = lambda x:x[1],reverse = True)))
    mydict = {
        'arr':arr,
        'globalcnt': globalcnt
    }
    return render(request,'index.html',context=mydict)