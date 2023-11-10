from django.shortcuts import render

# Create your views here.
def renderingone(request):
    return render(request,'renderingone.html')
def renderingtwo(request):
    return render(request,'renderingtwo.html')
def renderingthree(request):
    return render(request,'renderingthree.html')
def renderingfour(request):
    return render(request,'renderingfour.html')
