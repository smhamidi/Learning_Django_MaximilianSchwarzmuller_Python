from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthlyChallenges = {
    "january": "Spend At LEAST 5 minutes a day reading some books",
    "february": "Walk At LEAST for 20 minutes every single day",
    "march": "Work on solidity every day for the rest of this month",
    "april": "Spend At LEAST 5 minutes a day reading some books",
    "may": "Walk At LEAST for 20 minutes every single day",
    "june": "Work on solidity every day for the rest of this month",
    "july": "Spend At LEAST 5 minutes a day reading some books",
    "august": "Walk At LEAST for 20 minutes every single day",
    "september": "Work on solidity every day for the rest of this month",
    "october": "Spend At LEAST 5 minutes a day reading some books",
    "november": "Walk At LEAST for 20 minutes every single day",
    "december": "Work on solidity every day for the rest of this month",
}


# if the month value is integer, this function will trigger
def monthChallengeByNumber(request, month):
    try:
        redirectMonth = list(monthlyChallenges.keys())[month - 1]
    except:
        return HttpResponseNotFound("PAGE NOT FOUND")

    redirectPath = reverse("month-challenge", args=[redirectMonth])
    return HttpResponseRedirect(redirectPath)


# if the month value is string then this will get trigger
def monthChallenge(request, month):
    try:
        monthText = monthlyChallenges[month]
    except:
        return HttpResponseNotFound("PAGE NOT FOUND")
    responseText = f"<h1>{monthText}</h1>"
    return HttpResponse(responseText)


def challengePage(request):
    challengePageHTML = str()

    for monthName in monthlyChallenges.keys():
        monthPath = reverse("month-challenge", args=[monthName])
        challengePageHTML += (
            f"<li><h2><a href={monthPath}>challenge of {monthName}</a></h2></li>"
        )

    return HttpResponse(f"<ul>{challengePageHTML}</ul>")
