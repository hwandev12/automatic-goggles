from django.shortcuts import render
from .forms import *
from .models import *
from django.http import JsonResponse
from django.db.models import Avg, Max, Min
from django.db.models import Count

def home(request):
	rate = Rating.objects.filter(score=0).order_by("?").first()
	avg_rate = Rating.objects.aggregate(Avg("score"), Max("score"), Min("score"))
	context = {
		"rate": rate,
		"avg_rate": avg_rate,
	}
	return render(request, 'home.html', context)

def rate_image(request):
	if request.method == "POST":
		el_id = request.POST.get("el_id")
		val = request.POST.get("val")
		rate = Rating.objects.get(id=el_id)
		rate.score = val
		rate.save()
		return JsonResponse({"success": "true", "score": val}, safe=False)
	return JsonResponse({"success": "false"})