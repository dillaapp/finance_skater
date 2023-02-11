from django.urls import path, include
from . import views


app_name = 'financial_advisors'
urlpatterns = [
    path('financial_advisors/', views.fin_advisors, name="financial_advisors"),
    path('<int:fin_advisor_id>/book_an_advisor/', views.book_an_advisor, name="book_an_advisor"),
    path('book_appointment/', views.book_appointment, name="book_appointment"),
    path('booking_info/', views.booking_info, name="booking_info"),
]
