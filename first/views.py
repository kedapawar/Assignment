from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'a.html',{'title':'django','link':'http://youtube.com'})

def expression(request):
    a=int(request.GET['text1'])
    b=int(request.GET['text2'])
    c=a+b;
    return render(request,'output.html',{'result':c})