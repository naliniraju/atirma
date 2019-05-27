from rest_framework import serializers
from piatrika_form.models import *

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivisionModel
        #fields = ('id','division','sec_code','sec_name')
        fields ='__all__'

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        #fields = ('id','village_name','division_id','village_code')
        fields='__all__'

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ('id','csi_code',
        'sysno','csi_name',
        'city','ryot_photo',
        'rno','village_id',
        'litrary_status','person_id')


class LandVillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandVillage
        fields = ('id','land_village_code',
        'village_id','distance',
        'west','south',
        'land_village','plot_no',
        'east','north')

class APTSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationTreatment
        fields = ('id','date','farmer_land_village_id',
        'ssp','applied','mcp','application_treatment')

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
 
class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'
 
class FarmerBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerBank
        fields = '__all__'
 
class FarmerRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerRelation
        fields = '__all__'
 
class GuarantorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guarantor
        fields = '__all__'
 
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
 
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
 
class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'
 
class PlotVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotVisit
        fields = '__all__'
 
class VarietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Varietee
        fields = '__all__'
 
class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'
