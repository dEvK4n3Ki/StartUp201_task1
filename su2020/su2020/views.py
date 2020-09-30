from django.shortcuts import render

def homepage(request):
    return render(request,'su2020/index.html')