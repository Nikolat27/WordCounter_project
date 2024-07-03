import re
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@csrf_exempt
def home_page(request):
    if request.method == "POST":
        text = request.POST.get("text")
        words = text.split()
        total_characters = len(re.sub("a", "", text))
        total_words = len(words)
        return JsonResponse({"total_characters": total_characters, "total_words": total_words})
    else:
        return render(request, "word_app/index.html")
