from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    diction = {}
    return render(request, 'myapp/index.html',context=diction)
    


