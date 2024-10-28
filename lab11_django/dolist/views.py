from django.shortcuts import render


#create views here
def index(request):
    return render(request, 'index.html')