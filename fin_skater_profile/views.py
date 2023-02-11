from django.shortcuts import render


# Create your views here.
def index(request):
    # Rendering index page
    return render(request, "fin_skater_profile/index.html")


def about_us(request):
    # Rendering  about us page
    return render(request, "fin_skater_profile/about_us.html")
