from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "十二月",
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


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
        response_data = f"<h1>{monthly_challenges[month]}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
