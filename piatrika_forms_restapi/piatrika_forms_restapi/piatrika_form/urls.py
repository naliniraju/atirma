from django.contrib import admin
from django.urls import path
from piatrika_form import views
from django.conf.urls import url
  
urlpatterns = [ 
    url(r'^divisionmodels/$', views.division_view),
    url(r'^divisionmodels/(?P<pk>[0-9]+)$', views.division_detail),
    url(r'^villages/$', views.village_view),
    url(r'^villages/(?P<pk>[0-9]+)$', views.village_detail),
    url(r'^farmers/$', views.farmer_view),
    url(r'^farmers/(?P<pk>[0-9]+)$', views.farmer_detail),
    url(r'^landvillages/$', views.landvillage_view),
    url(r'^landvillages/(?P<pk>[0-9]+)$', views.landvillage_detail),
    url(r'^applicationtreatments/$', views.apt_view),
    url(r'^applicationtreatments/(?P<pk>[0-9]+)$', views.apt_detail),
    url(r'^banks/$', views.bank_view),
    url(r'^banks/(?P<pk>[0-9]+)$', views.bank_detail),
    url(r'^crops/$', views.crop_view),
    url(r'^crops/(?P<pk>[0-9]+)$', views.crop_detail),
    url(r'^farmerbanks/$', views.farmerbank_view),
    url(r'^farmerbanks/(?P<pk>[0-9]+)$', views.farmerbank_detail),
    url(r'^farmerrelations/$', views.farmerrelation_view),
    url(r'^farmerrelations/(?P<pk>[0-9]+)$', views.farmerrelation_detail),
    url(r'^guarantors/$', views.guarantor_view),
    url(r'^guarantors/(?P<pk>[0-9]+)$', views.guarantor_detail),
    url(r'^loans/$', views.loan_view),
    url(r'^loans/(?P<pk>[0-9]+)$', views.loan_detail),
    url(r'^persons/$', views.person_view),
    url(r'^persons/(?P<pk>[0-9]+)$', views.person_detail),
    url(r'^phones/$', views.phone_view),
    url(r'^phones/(?P<pk>[0-9]+)$', views.phone_detail),
    url(r'^plotvisits/$', views.plotvisit_view),
    url(r'^plotvisits/(?P<pk>[0-9]+)$', views.plotvisit_detail),
    url(r'^seasons/$', views.season_view),
    url(r'^seasons/(?P<pk>[0-9]+)$', views.season_detail),
    url(r'^varietees/$', views.variety_view),
    url(r'^varietees/(?P<pk>[0-9]+)$', views.variety_detail),
]
