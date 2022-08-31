from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "一月",
    "february": "二月",
    "march": "三月",
    "april": "四月",
    "may": "	五月",
    "june": "六月",
    "july": "七月",
    "august": "八月",
    "september": "九月",
    "october": "十月",
    "november": "十一月",
    "december": None,
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > 12:
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    # /challenges/january/
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month,
        })
    except:
        raise Http404()
