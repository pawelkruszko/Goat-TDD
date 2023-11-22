from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(
        request,
        "home.html",
        {"new item text": request.POST.get("item_text", "")},
    )
