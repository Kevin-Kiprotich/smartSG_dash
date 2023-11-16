from django.urls import path
from . import views

urlpatterns=[
    path("register/",views.Register.as_view(),name='register'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('assign/',views.AssignDriver.as_view(),name='driver'),
    path('report/',views.ReportOffence.as_view(),name='offence'),
    path('storelocation/',views.StoreLocation.as_view(),name='location'),
    path('track/',views.LocationsList.as_view(),name='track'),
    path('dashboard/',views.ShowOffences,name='dashboard'),
    path('offences/', views.OffenceList.as_view(), name='offence-list'),
]