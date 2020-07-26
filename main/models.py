from django.db import models


# Create your models here.

HAVE_BABY_CHOICES=(
    ('y','yes'),
    ('n','no'),
)

YN_CHOICES=(
    ('y','yes'),
    ('n','no'),
)

MONTH8_CHOICES=(
    ('JAN','JAN'),
    ('FEB','FEB'),
    ('MAR','MAR'),
    ('APR','APR'),
    ('MAY','MAY'),
    ('JUN','JUN'),
    ('JUL','JUL'),
    ('AUG','AUG'),
    ('SEP','SEP'),
    ('OCT','OCT'),
    ('NOV','NOV'),
    ('DEC','DEC'),
)

YEAR8_CHOICES=(
    ('2019','2019'),
    ('2020','2020'),
)

TIME9_D_CHOICES=(
    ('d','days'),
    ('m','months'),
    ('y','years')
)
class Patient(models.Model):


    
    name=models.CharField(max_length=100)
    email=models.EmailField(error_messages = {"@":"Please include a valid email address"})
    dob=models.DateField(default="0001-01-01",null=True,blank=True)
    weight=models.IntegerField(default=None,null=True,blank=True)
    height_feet=models.IntegerField(null=True,blank=True,default=0)
    height_inches=models.IntegerField(null=True,blank=True,default=0)
    waist=models.IntegerField(default=None,null=True,blank=True)
    hip=models.IntegerField(default=None,null=True,blank=True)
    
    have_baby=models.CharField(max_length=100,choices=HAVE_BABY_CHOICES,default='n')

    hyperprolactinemia=models.CharField(max_length=100,default='false',null=True,blank=True)
    pcos_pcod=models.CharField(max_length=100,default='false',null=True,blank=True)
    hypothyroidism=models.CharField(max_length=100,default='false',null=True,blank=True)
    
    
    



    

    weight9=models.IntegerField(null=True,blank=True,default=None)
    time9=models.IntegerField(null=True,blank=True,default=None)
    time9_d=models.CharField(max_length=100,choices=TIME9_D_CHOICES,default='m')
    stoppedPeriods=models.CharField(max_length=100,null=True,blank=True,default='false')
    lessThanSixCycles=models.CharField(max_length=100,null=True,blank=True,default='false')
    moreThanSixCycles=models.CharField(max_length=100,null=True,blank=True,default='false')
    countinuosFlow=models.CharField(max_length=100,null=True,blank=True,default='false')
    

    currentlyNotUnderAnyMedication=models.CharField(max_length=100,null=True,blank=True,default='false')
    diabestes=models.CharField(max_length=100,null=True,blank=True,default='false')
    migrane=models.CharField(max_length=100,null=True,blank=True,default='false')
    medicationHighBloodPressure=models.CharField(max_length=100,null=True,blank=True,default='false')
    medicationMentalHealthDisorder=models.CharField(max_length=100,null=True,blank=True,default='false')
    steroidTherapy=models.CharField(max_length=100,null=True,blank=True,default='false')
    hormonalContraception=models.CharField(max_length=100,null=True,blank=True,default='false')
    seizure=models.CharField(max_length=100,null=True,blank=True,default='false')
    proteinSupplements=models.CharField(max_length=100,null=True,blank=True,default='false')
    Opioids=models.CharField(max_length=100,null=True,blank=True,default='false')
    antiHistamines=models.CharField(max_length=100,null=True,blank=True,default='false')

    
    
    
   

    undergoneSurgery=models.CharField(max_length=100,null=True,blank=True,default='false')
    physicallyImmobile=models.CharField(max_length=100,null=True,blank=True,default='false')
    viralFever=models.CharField(max_length=100,null=True,blank=True,default='false')

    workoutValue=models.CharField(max_length=100,choices=YN_CHOICES,default='n')
    eatFoodValue=models.CharField(max_length=100,choices=YN_CHOICES,default='n')

    sleepValue=models.IntegerField(null=True,blank=True,default=0)
    

    highBloodPressure=models.CharField(max_length=100,null=True,blank=True,default='false')
    highCholesterol=models.CharField(max_length=100,null=True,blank=True,default='false')
    familyHypothyroidism=models.CharField(max_length=100,null=True,blank=True,default='false')
    diabetes=models.CharField(max_length=100,null=True,blank=True,default='false')
    pcos=models.CharField(max_length=100,null=True,blank=True,default='false')

   
    

    hairLoss=models.CharField(max_length=100,null=True,blank=True,default='false')
   

    acneLoss=models.CharField(max_length=100,null=True,blank=True,default='false')
    

    missedPeriod=models.CharField(max_length=100,null=True,blank=True,default='false')
   

    extraHair=models.CharField(max_length=100,null=True,blank=True,default='false')
   

    constipation=models.CharField(max_length=100,null=True,blank=True,default='false')

    skinPigmentation=models.CharField(max_length=100,null=True,blank=True,default='false')

    slowHeartbeat=models.CharField(max_length=100,null=True,blank=True,default='false')

    headache=models.CharField(max_length=100,null=True,blank=True,default='false')
    

    dischargeNipple=models.CharField(max_length=100,null=True,blank=True,default='false')

    moodSwings=models.CharField(max_length=100,null=True,blank=True,default='false')

    




    
    


