from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def Home(request):
    return render(request, 'GH2h_Home/home.html')