from django.db import models
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
Status_type=(
    ("Normal","Normal"),
    ("Disabled","Disabled"),

)

class Users(models.Model):
    user_id=models.IntegerField(_("User_ID"))
    status=models.CharField(_("Status"),max_length=10,choices=Status_type)

    def __str__(self):
        return str(self.user_id)
class Station(models.Model):
    fid=models.IntegerField(_("Fid"))
    id=models.IntegerField(_("Id"),unique=True,primary_key=True)
    name=models.CharField(_("Name"),max_length=40)
    def __str__(self):
        return self.name
class FamousPlace(models.Model):
    station = models.ForeignKey("Station", related_name='station_place', on_delete=models.SET_NULL,null=True)
    name = models.CharField(_("Name"),max_length=100)

    def __str__(self):
        return self.name
    

class Roads(models.Model):
    fid=models.IntegerField(_("FID"))
    id=models.IntegerField(_("ID"),unique=True,primary_key=True)
    geometry = models.LineStringField()
    name=models.CharField(_("Name"),max_length=40)
    time=models.IntegerField(_("Time"))
    distance=models.FloatField(_("Distane"),max_length=15)
    def __str__(self):
        return self.name    

class Ticket(models.Model):
    from_station = models.ForeignKey(Station, related_name='from_station', on_delete=models.SET_NULL,null=True)
    to_station = models.ForeignKey(Station, related_name='to_station', on_delete=models.SET_NULL,null=True)
    cost = models.IntegerField(_("Cost"))
    time = models.FloatField(_("Time"))


    

    
        
