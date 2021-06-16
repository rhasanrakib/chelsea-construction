
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_view,name="home" ),
    path('about/',views.about_view,name="about" ),
    path('contact/',views.contact_view,name="contact" ),
    path('portfolio/',views.portfolio_view,name="portfolio" ),
    path('approach/',views.approach_view,name="approach"),
    path('service/',views.service_view,name="service"),
    path('service/',views.service_view,name="service"),
    path('refurbishment/',views.refurbish_view,name="refurbish"),
    path('maintenance/',views.maintenance_view,name="maintenance"),
    path('private_residence/',views.private_residence_view,name="private_residence"),
    
]
