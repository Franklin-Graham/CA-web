from django.shortcuts import render,redirect

# Create your views here.
def fun1(request):
    return render(request,'index.html')
def Detail(request):
    return render(request,'details.html')
def Bot(request):
    return render(request,'bots.html')



