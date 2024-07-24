# booking/views.py

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return render(request, 'thanks.html', {'name': name})
    return render(request, 'index.html')

def thanks(request):
    return HttpResponse("Thank you for your submission!")
