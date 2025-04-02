from django.urls import path
from .views import (CompanyListAPIView, CompanyDetailAPIView, CompanyVacanciesAPIView,
                    VacancyListAPIView, VacancyDetailAPIView, TopTenVacanciesAPIView)

urlpatterns = [
    path('companies/', CompanyListAPIView.as_view(), name='all_companies'),
    path('companies/<int:id>/', CompanyDetailAPIView.as_view(), name='company'),
    path('companies/<int:id>/vacancies/', CompanyVacanciesAPIView.as_view(), name='company_vacancies'),
    path('vacancies/', VacancyListAPIView.as_view(), name='all_vacancies'),
    path('vacancies/<int:id>/', VacancyDetailAPIView.as_view(), name='vacancy'),
    path('vacancies/top_ten/', TopTenVacanciesAPIView.as_view(), name='top_ten_vacancies')
]