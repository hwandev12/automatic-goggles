from django.shortcuts import render
from .forms import *
from .models import *

def home(request):
	rate = Rating.objects.filter(score=3).order_by("?").first()
	context = {
		"rate": rate
	}
	return render(request, 'home.html', context)
