from django.shortcuts import render
from .models import BioData
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    students = BioData.objects.all()
    context = {
        'students': students
    }
    return render(request, 'home.html', context)



