from django.db import models  

class Farmer(models.Model):  
    csi_code   = models.CharField(max_length=20)  
    sysno 	   = models.CharField(max_length=20)  
    csi_name   = models.CharField(max_length=20)  
    city 	   = models.CharField(max_length=20)
    ryot_photo = models.ImageField(blank = True, null = True)
    rno 	   = models.CharField(max_length=20)  
    village_id = models.CharField(max_length=20)
    litrary_status = models.CharField(max_length=20)
    person_id  = models.CharField(max_length=20)
    #
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    LatLng = models.CharField(max_length=255)
    class Meta:  
        db_table = "farmers"
 

 
class DivisionModel(models.Model):  
    division = models.CharField(max_length=20)  
    section_code = models.CharField(max_length=20)  
    section_name = models.CharField(max_length=20)  
    class Meta:  
        db_table = "divisionmodels"
 
class Village(models.Model):
    division_id  = models.CharField(max_length=20)  
    village_name = models.CharField(max_length=100)
    village_code = models.CharField(max_length=100)    
    class Meta:  
        db_table = "villages"

class LandVillage(models.Model):  
    land_village_code = models.CharField(max_length=20)
    village_id = models.CharField(max_length=20)
    distance = models.CharField(max_length=20)
    west = models.CharField(max_length=20)
    south = models.CharField(max_length=20)
    land_village = models.CharField(max_length=20)
    plot_no = models.CharField(max_length=20)
    east = models.CharField(max_length=20)
    north = models.CharField(max_length=20)
    class Meta:  
        db_table = "landvillages"
 
class ApplicationTreatment(models.Model):  
    date = models.DateField(blank=True,null=True) #  
    farmer_land_village_id = models.PositiveIntegerField() #  
    ssp = models.CharField(max_length=20)  
    applied = models.CharField(max_length=20)
    mcp = models.CharField(max_length=20)
    application_treatment = models.CharField(max_length=20) #
    class Meta:  
        db_table = "applicationtreatments"

class Bank(models.Model):
    bank = models.CharField(max_length=70, blank=False, default='')
    bank_code = models.CharField(max_length=70, blank=False, default='')
    branch_address = models.CharField(max_length=70, blank=False, default='')
   
    class Meta:  
        db_table = "banks"
 
class Crop(models.Model):
    crop_name = models.CharField(max_length=70, blank=False, default='')
    crop_scientific_name = models.CharField(max_length=70, blank=False, default='')
    class Meta:  
        db_table = "crops"
 
class FarmerBank(models.Model):
    account_no = models.CharField(max_length=70, blank=False, default='')
    Farmers_id = models.CharField(max_length=70, blank=False, default='') #
    bank_id = models.CharField(max_length=70, blank=False, default='')
    class Meta:  
        db_table = "farmerbanks"
 
class FarmerRelation(models.Model):
    related_to_csi = models.CharField(max_length=70, blank=False, default='')
    person_id = models.PositiveIntegerField() #
    relationship_type = models.CharField(max_length=70, blank=False, default='')
    class Meta:  
        db_table = "farmerrelations"
 
class Guarantor(models.Model):
    season_id = models.CharField(max_length=70, blank=False, default='')
    season_farmer_id = models.CharField(max_length=70, blank=False, default='')
    season_land_village_id = models.CharField(max_length=70, blank=False, default='')
    person_id = models.CharField(max_length=70, blank=False, default='')
    class Meta:  
        db_table = "guarantors"
 
class Loan(models.Model):
    sb_acno = models.CharField(max_length=70, blank=False, default='')
    ledger_no = models.CharField(max_length=70, blank=False, default='')
    folio_no = models.CharField(max_length=70, blank=False, default='')
    Farmers_id = models.CharField(max_length=70, blank=False, default='') #
    loan_no = models.CharField(max_length=70, blank=False, default='')
    loan_ac_ledger_no = models.CharField(max_length=70, blank=False, default='')
    loan_ac_folio_no = models.CharField(max_length=70, blank=False, default='')
    payment_mode = models.CharField(max_length=70, blank=False, default='')
    class Meta:  
        db_table = "loans"
 
class Person(models.Model):
    first_name = models.CharField(max_length=70, blank=False, default='')
    last_name = models.CharField(max_length=70, blank=False, default='')
    middle_name = models.CharField(max_length=70, blank=False, default='')
    city = models.CharField(max_length=70, blank=False, default='')
    address = models.CharField(max_length=70, blank=False, default='')
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True) #
    class Meta:  
        db_table = "persons"
 
class Phone(models.Model):
    phone_type = models.CharField(max_length=70, blank=False, default='')
    number = models.CharField(max_length=70, blank=False, default='')
    person_id = models.CharField(max_length=70, blank=False, default='')
    class Meta:  
        db_table = "phones"
 
class PlotVisit(models.Model):
    condition = models.CharField(max_length=70, blank=False, default='')
    advice_given = models.CharField(max_length=70, blank=False, default='')
    identification = models.CharField(max_length=70, blank=False, default='')
    time_stamp = models.DateField(blank=True,null=True)
    season_id = models.CharField(max_length=70, blank=False, default='')
 
    class Meta:  
        db_table = "plotvisits"
 
class Varietee(models.Model):
    variety = models.CharField(max_length=70, blank=False, default='')
    crop_id = models.CharField(max_length=70, blank=False, default='')
    variety_scientific_name = models.CharField(max_length=70, blank=False, default='')
    class Meta:  
        db_table = "varietees"
 
class Season(models.Model):
    season_start = models.DateField(blank=True,null=True)
    extent = models.CharField(max_length=70, blank=False, default='')
    expected_harvesting = models.DateField(blank=True,null=True) #
    expected_planting = models.DateField(blank=True,null=True) #
    Farmers_id = models.PositiveIntegerField() #
    land_village_id = models.PositiveIntegerField() #
    current_variety = models.CharField(max_length=70, blank=False, default='')
    previous_variety = models.CharField(max_length=70, blank=False, default='')
    plant_type = models.CharField(max_length=70, blank=False, default='')
    total_acres = models.CharField(max_length=70, blank=False, default='')
    measurement_acres = models.CharField(max_length=70, blank=False, default='')
    estimated_yield = models.CharField(max_length=70, blank=False, default='')
    offer_no = models.CharField(max_length=70, blank=False, default='')
    offer_date = models.DateField(blank=True,null=True) #
    agreement_date = models.DateField(blank=True,null=True)
    agreement_acre = models.IntegerField() #
    agreement_tonne = models.IntegerField() #
    class Meta:  
        db_table = "seasons"