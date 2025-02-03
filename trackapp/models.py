from django.db import models

# Create your models here.
class tracker(models.Model):
    Circle=models.CharField(max_length=100)
    Old_site_id=models.CharField(max_length=100)
    New_Site_Id=models.CharField(max_length=100)
    Integration_Date=models.DateField()	
    MS1_Date=models.DateField()	
    Old_site_technology=models.CharField(max_length=100)
    Allocated_technology=models.CharField(max_length=100)
    Deployed_technology_Deviation=models.CharField(max_length=100)
    No_of_deviated_tech=models.CharField(max_length=100)
    Old_site_locked_date=models.DateField()
    New_site_unlock_date=models.DateField()
    Old_site_traffic=models.CharField(max_length=100)
    Existing_traffic=models.CharField(max_length=100)
    Old_site_admin_status=models.CharField(max_length=100)
    New_site_admin_status=models.CharField(max_length=100)
    Both_site_unlocked=models.CharField(max_length=100)
    Both_site_locked=models.CharField(max_length=100)
    Pre_less_then_3_Mbps=models.CharField(max_length=100)
    Current_less_then_3_Mbps=models.CharField(max_length=100)

def __str__(self):
    return self.Circle


  