from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import *


# Create your views here.
def fin_advisors(request):
    financial_advisors_list = FinAdvisors.objects.order_by('-pub_date')[:20]
    context = {'financial_advisors_list': financial_advisors_list}
    return render(request, "financial_advisors/financial_advisors.html", context)


@login_required
def book_an_advisor(request, fin_advisor_id):
    financial_advisor = get_object_or_404(FinAdvisors, pk=fin_advisor_id)
    context = {'financial_advisor': financial_advisor}
    return render(request, "financial_advisors/book_an_advisor.html", context)


@login_required
def booking_info(request):
    booking_list = Booking.objects.order_by('-booking_date')[:3]
    context = {'booking_list': booking_list}
    return render(request, "financial_advisors/booking_info.html", context)


@login_required
def book_appointment(request):
    if request.method == "POST":
        fin_advisor_username = request.POST['fin_advisor_username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        day_and_time = request.POST['day_and_time']
        location = request.POST['location']
        topic = request.POST['topic']
        booking = Booking(fin_advisor_username=fin_advisor_username, first_name=first_name, email=email,
                          day_and_time=day_and_time,
                          location=location, topic=topic)
        booking.save()

    return render(request, 'financial_advisors/booking_success.html')
