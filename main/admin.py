from django.contrib import admin
from main.models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display=['name','email','dob','weight','height_feet','height_inches','waist','hip','have_baby',
    'hyperprolactinemia','pcos_pcod','hypothyroidism',
    'weight9','time9','time9_d','stoppedPeriods','lessThanSixCycles','moreThanSixCycles','countinuosFlow',
    'currentlyNotUnderAnyMedication',

    'diabestes',
    

    'migrane',
    

    'medicationHighBloodPressure',
    

    'medicationMentalHealthDisorder',
    
    'steroidTherapy',
    

    'hormonalContraception',
    

    'seizure',
    

    'proteinSupplements',
    

    'Opioids',
    

    'antiHistamines',
    

    

    'undergoneSurgery',
    'physicallyImmobile',
    'viralFever',

    'workoutValue',
    'eatFoodValue',

    'sleepValue',
    

    'highBloodPressure',
    'highCholesterol',
    'familyHypothyroidism',
    'diabetes',
    'pcos',

    

    'hairLoss',
    

    'acneLoss',
    

    'missedPeriod',
    

    'extraHair',
   
    'constipation',

    'skinPigmentation',

    'slowHeartbeat',

    'headache',
    
    'dischargeNipple',

    'moodSwings',





    


    ]


class DoctorOutputAdmin(admin.ModelAdmin):
    list_display=['patient_email']

admin.site.register(
    Patient,
    PatientAdmin,
    
)

