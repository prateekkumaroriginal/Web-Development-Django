from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

challenges = {
    "january": "Walk at least 5km everyday in the evening.",
    "february": "Increase the daily walking distance to 7km.",
    "march": "Try a new workout routine or exercise class at least twice a week.",
    "april": "Incorporate strength training exercises into your routine three times a week.",
    "may": "Complete a 30-day fitness challenge, such as a plank challenge or a squat challenge.",
    "june": "Explore different outdoor activities, such as hiking or cycling, on the weekends.",
    "july": "Join a sports team or club and participate in regular practices and games.",
    "august": "Aim to run for at least 3km three times a week.",
    "september": "Take up a new physical hobby, such as dancing or martial arts, and attend classes regularly.",
    "october": "Set a goal to complete a 10km run or walk by the end of the month.",
    "november": "Focus on flexibility and balance by incorporating yoga or Pilates sessions into your weekly routine.",
    "december": "Engage in winter sports, such as skiing or ice skating, at least once a week.",
}


def monthly_challenge_by_number(request, month):
    if month > len(challenges):
        return HttpResponseNotFound("Invalid Month!!")
    months = list(challenges.keys())
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    if month in challenges:
        challenge_text = challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month,
        })
    else:
        raise Http404()


def index_page(request):
    months = list(challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

