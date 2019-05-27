from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime

#from .models import Division,Village, LandVillage, Farmer, ApplicationTreatment
#from .forms import VillageForm, DivisionForm, LandVillageForm, FarmerForm, APTForm

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status

from piatrika_form.models import *
from piatrika_form.serializers import *

 
@csrf_exempt
def division_view(request):
    if request.method == 'GET':
        divisions = DivisionModel.objects.all()
        division_serializer = DivisionSerializer(divisions, many=True)
        return JsonResponse(division_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
 
    elif request.method == 'POST':
        division_data = JSONParser().parse(request)
        division_serializer = DivisionSerializer(data=division_data)
        if division_serializer.is_valid():
            division_serializer.save()
            return JsonResponse(division_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(division_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        DivisionModel.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt 
def division_detail(request, pk):
    try: 
        divisions = DivisionModel.objects.get(pk=pk) 
    except DivisionModel.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    # try: 
    #     ryot = Ryot.objects.get(pk=pk) 
    # except Ryot.DoesNotExist: 
    #     return HttpResponse(status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'GET': 
        division_serializer = DivisionSerializer(divisions) 
        return JsonResponse(division_serializer.data) 

        # ryot_serializer = RyotSerializer(ryot) 
        # return JsonResponse(ryot_serializer.data)

    elif request.method == 'PUT': 
        division_data = JSONParser().parse(request) 
        division_serializer = DivisionSerializer(divisions, data=division_data) 
        if division_serializer.is_valid(): 
            division_serializer.save() 
            return JsonResponse(division_serializer.data) 
        return JsonResponse(division_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        # ryot_data = JSONParser().parse(request) 
        # ryot_serializer = RyotSerializer(ryot, data=ryot_data) 
        # if ryot_serializer.is_valid(): 
        #     ryot_serializer.save() 
        #     return JsonResponse(ryot_serializer.data) 
        # return JsonResponse(ryot_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        divisions.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

        # ryot.delete() 
        # return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def village_view(request):
    if request.method == 'GET':
        villages = Village.objects.all()
        village_serializer = VillageSerializer(villages, many=True)
        return JsonResponse(village_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
 
    elif request.method == 'POST':
        village_data = JSONParser().parse(request)
        village_serializer = VillageSerializer(data=village_data)
        if village_serializer.is_valid():
            village_serializer.save()
            return JsonResponse(village_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(village_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        Village.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt 
def village_detail(request, pk):
    try: 
        villages = Village.objects.get(pk=pk) 
    except Village.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        village_serializer = VillageSerializer(villages) 
        return JsonResponse(village_serializer.data) 

    elif request.method == 'PUT': 
        village_data = JSONParser().parse(request) 
        village_serializer = VillageSerializer(villages, data=village_data) 
        if village_serializer.is_valid(): 
            village_serializer.save() 
            return JsonResponse(village_serializer.data) 
        return JsonResponse(village_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        villages.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def farmer_view(request):
    if request.method == 'GET':
        farmers = Farmer.objects.all()
        farmer_serializer = FarmerSerializer(farmers, many=True)
        return JsonResponse(farmer_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
 
    elif request.method == 'POST':
        farmer_data = JSONParser().parse(request)
        farmer_serializer = FarmerSerializer(data=farmer_data)
        if farmer_serializer.is_valid():
            farmer_serializer.save()
            return JsonResponse(farmer_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(farmer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        Farmer.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt 
def farmer_detail(request, pk):
    try: 
        farmers = Farmer.objects.get(pk=pk) 
    except Farmer.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        farmer_serializer = FarmerSerializer(farmers) 
        return JsonResponse(farmer_serializer.data) 

    elif request.method == 'PUT': 
        farmer_data = JSONParser().parse(request) 
        farmer_serializer = FarmerSerializer(farmers, data=farmer_data) 
        if farmer_serializer.is_valid(): 
            farmer_serializer.save() 
            return JsonResponse(farmer_serializer.data) 
        return JsonResponse(farmer_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        farmers.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def landvillage_view(request):
    if request.method == 'GET':
        landvillages = LandVillage.objects.all()
        landvillage_serializer = LandVillageSerializer(landvillages, many=True)
        return JsonResponse(landvillage_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
 
    elif request.method == 'POST':
        landvillage_data = JSONParser().parse(request)
        landvillage_serializer = LandVillageSerializer(data=landvillage_data)
        if landvillage_serializer.is_valid():
            landvillage_serializer.save()
            return JsonResponse(landvillage_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(landvillage_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        LandVillage.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt 
def landvillage_detail(request, pk):
    try: 
        landvillages = LandVillage.objects.get(pk=pk) 
    except LandVillage.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        landvillage_serializer = LandVillageSerializer(landvillages) 
        return JsonResponse(landvillage_serializer.data) 

    elif request.method == 'PUT': 
        landvillage_data = JSONParser().parse(request) 
        landvillage_serializer = LandVillageSerializer(landvillages, data=landvillage_data) 
        if landvillage_serializer.is_valid(): 
            landvillage_serializer.save() 
            return JsonResponse(landvillage_serializer.data) 
        return JsonResponse(landvillage_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        landvillages.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)



@csrf_exempt
def apt_view(request):
    if request.method == 'GET':
        apts = ApplicationTreatment.objects.all()
        apt_serializer = APTSerializer(apts, many=True)
        return JsonResponse(apt_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
 
    elif request.method == 'POST':
        apt_data = JSONParser().parse(request)
        apt_serializer = APTSerializer(data=apt_data)
        if apt_serializer.is_valid():
            apt_serializer.save()
            return JsonResponse(apt_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(apt_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        ApplicationTreatment.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt 
def apt_detail(request, pk):
    try: 
        apts = ApplicationTreatment.objects.get(pk=pk) 
    except ApplicationTreatment.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        apt_serializer = APTSerializer(apts) 
        return JsonResponse(apt_serializer.data) 

    elif request.method == 'PUT': 
        apt_data = JSONParser().parse(request) 
        apt_serializer = APTSerializer(apts, data=apt_data) 
        if apt_serializer.is_valid(): 
            apt_serializer.save() 
            return JsonResponse(apt_serializer.data) 
        return JsonResponse(apt_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        apts.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

###
###
###

@csrf_exempt
def bank_view(request):
    if request.method == 'GET':
        banks = Bank.objects.all()
        bank_serializer = BankSerializer(banks, many=True)
        return JsonResponse(bank_serializer.data, safe=False)
        
    elif request.method == 'POST':
        bank_data = JSONParser().parse(request)
        bank_serializer = BankSerializer(data=bank_data)
        if bank_serializer.is_valid():
            bank_serializer.save()
            return JsonResponse(bank_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(bank_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Bank.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)        
 
 
@csrf_exempt 
def bank_detail(request, pk):
    try: 
        bank = Bank.objects.get(pk=pk) 
    except Bank.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        bank_serializer = BankSerializer(bank) 
        return JsonResponse(bank_serializer.data) 

    elif request.method == 'PUT': 
        bank_data = JSONParser().parse(request) 
        bank_serializer = BankSerializer(bank, data=bank_data) 
        if bank_serializer.is_valid(): 
            bank_serializer.save() 
            return JsonResponse(bank_serializer.data) 
        return JsonResponse(bank_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        bank.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def crop_view(request):
    if request.method == 'GET':
        crops = Crop.objects.all()
        crop_serializer = CropSerializer(crops, many=True)
        return JsonResponse(crop_serializer.data, safe=False)
        
    elif request.method == 'POST':
        crop_data = JSONParser().parse(request)
        crop_serializer = CropSerializer(data=crop_data)
        if crop_serializer.is_valid():
            crop_serializer.save()
            return JsonResponse(crop_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(crop_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Crop.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)        
 
 
@csrf_exempt 
def crop_detail(request, pk):
    try: 
        crop = Crop.objects.get(pk=pk) 
    except Crop.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        crop_serializer = CropSerializer(crop) 
        return JsonResponse(crop_serializer.data) 

    elif request.method == 'PUT': 
        crop_data = JSONParser().parse(request) 
        crop_serializer = CropSerializer(crop, data=crop_data) 
        if crop_serializer.is_valid(): 
            crop_serializer.save() 
            return JsonResponse(crop_serializer.data) 
        return JsonResponse(crop_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        crop.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def farmerbank_view(request):
    if request.method == 'GET':
        farmerbanks = FarmerBank.objects.all()
        farmerbank_serializer = FarmerBankSerializer(farmerbanks, many=True)
        return JsonResponse(farmerbank_serializer.data, safe=False)
        
    elif request.method == 'POST':
        farmerbank_data = JSONParser().parse(request)
        farmerbank_serializer = FarmerBankSerializer(data=farmerbank_data)
        if farmerbank_serializer.is_valid():
            farmerbank_serializer.save()
            return JsonResponse(farmerbank_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(farmerbank_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        FarmerBank.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)        
 
 
@csrf_exempt 
def farmerbank_detail(request, pk):
    try: 
        farmerbank = FarmerBank.objects.get(pk=pk) 
    except FarmerBank.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        farmerbank_serializer = FarmerBankSerializer(farmerbank) 
        return JsonResponse(farmerbank_serializer.data) 

    elif request.method == 'PUT': 
        farmerbank_data = JSONParser().parse(request) 
        farmerbank_serializer = FarmerBankSerializer(farmerbank, data=farmerbank_data) 
        if farmerbank_serializer.is_valid(): 
            farmerbank_serializer.save() 
            return JsonResponse(farmerbank_serializer.data) 
        return JsonResponse(farmerbank_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        farmerbank.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def farmerrelation_view(request):
    if request.method == 'GET':
        farmerrelations = FarmerRelation.objects.all()
        farmerrelation_serializer = FarmerRelationSerializer(farmerrelations, many=True)
        return JsonResponse(farmerrelation_serializer.data, safe=False)
        
    elif request.method == 'POST':
        farmerrelation_data = JSONParser().parse(request)
        farmerrelation_serializer = FarmerRelationSerializer(data=farmerrelation_data)
        if farmerrelation_serializer.is_valid():
            farmerrelation_serializer.save()
            return JsonResponse(farmerrelation_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(farmerrelation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        FarmerRelation.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)        
 
 
@csrf_exempt 
def farmerrelation_detail(request, pk):
    try: 
        farmerrelation = FarmerRelation.objects.get(pk=pk) 
    except FarmerRelation.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        farmerrelation_serializer = FarmerRelationSerializer(farmerrelation) 
        return JsonResponse(farmerrelation_serializer.data) 

    elif request.method == 'PUT': 
        farmerrelation_data = JSONParser().parse(request) 
        farmerrelation_serializer = FarmerRelationSerializer(farmerrelation, data=farmerrelation_data) 
        if farmerrelation_serializer.is_valid(): 
            farmerrelation_serializer.save() 
            return JsonResponse(farmerrelation_serializer.data) 
        return JsonResponse(farmerrelation_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        farmerrelation.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def guarantor_view(request):
    if request.method == 'GET':
        guarantors = Guarantor.objects.all()
        guarantor_serializer = GuarantorSerializer(guarantors, many=True)
        return JsonResponse(guarantor_serializer.data, safe=False)
        
    elif request.method == 'POST':
        guarantor_data = JSONParser().parse(request)
        guarantor_serializer = GuarantorSerializer(data=guarantor_data)
        if guarantor_serializer.is_valid():
            guarantor_serializer.save()
            return JsonResponse(guarantor_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(guarantor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Guarantor.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)        
 
 
@csrf_exempt 
def guarantor_detail(request, pk):
    try: 
        guarantor = Guarantor.objects.get(pk=pk) 
    except Guarantor.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        guarantor_serializer = GuarantorSerializer(guarantor) 
        return JsonResponse(guarantor_serializer.data) 

    elif request.method == 'PUT': 
        guarantor_data = JSONParser().parse(request) 
        guarantor_serializer = GuarantorSerializer(guarantor, data=guarantor_data) 
        if guarantor_serializer.is_valid(): 
            guarantor_serializer.save() 
            return JsonResponse(guarantor_serializer.data) 
        return JsonResponse(guarantor_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        guarantor.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def loan_view(request):
    if request.method == 'GET':
        loans = Loan.objects.all()
        loan_serializer = LoanSerializer(loans, many=True)
        return JsonResponse(loan_serializer.data, safe=False)
        
    elif request.method == 'POST':
        loan_data = JSONParser().parse(request)
        loan_serializer = LoanSerializer(data=loan_data)
        if loan_serializer.is_valid():
            loan_serializer.save()
            return JsonResponse(loan_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(loan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Loan.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)        
 
 
@csrf_exempt 
def loan_detail(request, pk):
    try: 
        loan = Loan.objects.get(pk=pk) 
    except Loan.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        loan_serializer = LoanSerializer(loan) 
        return JsonResponse(loan_serializer.data) 

    elif request.method == 'PUT': 
        loan_data = JSONParser().parse(request) 
        loan_serializer = LoanSerializer(loan, data=loan_data) 
        if loan_serializer.is_valid(): 
            loan_serializer.save() 
            return JsonResponse(loan_serializer.data) 
        return JsonResponse(loan_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        loan.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def person_view(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        person_serializer = PersonSerializer(persons, many=True)
        return JsonResponse(person_serializer.data, safe=False)
        
    elif request.method == 'POST':
        person_data = JSONParser().parse(request)
        person_serializer = PersonSerializer(data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse(person_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Person.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)        
 
 
@csrf_exempt 
def person_detail(request, pk):
    try: 
        person = Person.objects.get(pk=pk) 
    except Person.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        person_serializer = PersonSerializer(person) 
        return JsonResponse(person_serializer.data) 

    elif request.method == 'PUT': 
        person_data = JSONParser().parse(request) 
        person_serializer = PersonSerializer(person, data=person_data) 
        if person_serializer.is_valid(): 
            person_serializer.save() 
            return JsonResponse(person_serializer.data) 
        return JsonResponse(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        person.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def phone_view(request):
    if request.method == 'GET':
        phones = Phone.objects.all()
        phone_serializer = PhoneSerializer(phones, many=True)
        return JsonResponse(phone_serializer.data, safe=False)
        
    elif request.method == 'POST':
        phone_data = JSONParser().parse(request)
        phone_serializer = PhoneSerializer(data=phone_data)
        if phone_serializer.is_valid():
            phone_serializer.save()
            return JsonResponse(phone_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(phone_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Phone.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)        
 
 
@csrf_exempt 
def phone_detail(request, pk):
    try: 
        phone = Phone.objects.get(pk=pk) 
    except Phone.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        phone_serializer = PhoneSerializer(phone) 
        return JsonResponse(phone_serializer.data) 

    elif request.method == 'PUT': 
        phone_data = JSONParser().parse(request) 
        phone_serializer = PhoneSerializer(phone, data=phone_data) 
        if phone_serializer.is_valid(): 
            phone_serializer.save() 
            return JsonResponse(phone_serializer.data) 
        return JsonResponse(phone_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        phone.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def plotvisit_view(request):
    if request.method == 'GET':
        plotvisits = PlotVisit.objects.all()
        plotvisit_serializer = PlotVisitSerializer(plotvisits, many=True)
        return JsonResponse(plotvisit_serializer.data, safe=False)
        
    elif request.method == 'POST':
        plotvisit_data = JSONParser().parse(request)
        plotvisit_serializer = PlotVisitSerializer(data=plotvisit_data)
        if plotvisit_serializer.is_valid():
            plotvisit_serializer.save()
            return JsonResponse(plotvisit_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(plotvisit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        PlotVisit.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)        
 
 
@csrf_exempt 
def plotvisit_detail(request, pk):
    try: 
        plotvisit = PlotVisit.objects.get(pk=pk) 
    except PlotVisit.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'GET': 
        plotvisit_serializer = PlotVisitSerializer(plotvisit) 
        return JsonResponse(plotvisit_serializer.data) 

    elif request.method == 'PUT': 
        plotvisit_data = JSONParser().parse(request) 
        plotvisit_serializer = PlotVisitSerializer(plotvisit, data=plotvisit_data) 
        if plotvisit_serializer.is_valid(): 
            plotvisit_serializer.save() 
            return JsonResponse(plotvisit_serializer.data) 
        return JsonResponse(plotvisit_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        plotvisit.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def variety_view(request):
    if request.method == 'GET':
        varieties = Varietee.objects.all()
        variety_serializer = VarietySerializer(varieties, many=True)
        return JsonResponse(variety_serializer.data, safe=False)
   
    elif request.method == 'POST':
        variety_data = JSONParser().parse(request)
        variety_serializer = VarietySerializer(data=variety_data)
        if variety_serializer.is_valid():
            variety_serializer.save()
            return JsonResponse(variety_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(variety_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE':
        Varietee.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
       
 
 
@csrf_exempt
def variety_detail(request, pk):
    try:
        variety = Varietee.objects.get(pk=pk)
    except Varietee.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'GET':
        variety_serializer = VarietySerializer(variety)
        return JsonResponse(variety_serializer.data)
 
 
    elif request.method == 'PUT':
        variety_data = JSONParser().parse(request)
        variety_serializer = VarietySerializer(variety, data=variety_data)
        if variety_serializer.is_valid():
            variety_serializer.save()
            return JsonResponse(variety_serializer.data)
        return JsonResponse(variety_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'DELETE':
        variety.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
 
 
 
@csrf_exempt
def season_view(request):
    if request.method == 'GET':
        seasons = Season.objects.all()
        seasons_serializer = SeasonSerializer(seasons, many=True)
        return JsonResponse(seasons_serializer.data, safe=False)
        
    elif request.method == 'POST':
        seasons_data = JSONParser().parse(request)
        seasons_serializer = SeasonSerializer(data=seasons_data)
        if seasons_serializer.is_valid():
            seasons_serializer.save()
            return JsonResponse(seasons_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(seasons_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
        
    elif request.method == 'DELETE':
        Season.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
            
 
 
@csrf_exempt
def season_detail(request, pk):
    try:
        season = Season.objects.get(pk=pk)
    except Season.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'GET':
        season_serializer = SeasonSerializer(season)
        return JsonResponse(season_serializer.data)
 
    elif request.method == 'PUT':
        season_data = JSONParser().parse(request)
        season_serializer = SeasonSerializer(season, data=season_data)
        if season_serializer.is_valid():
            season_serializer.save()
            return JsonResponse(season_serializer.data)
        return JsonResponse(season_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE':
        season.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
 