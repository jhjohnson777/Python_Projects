from django.db import models

# Create your models here.
class UniversityCampus(models.Model): #creates class UniversityCampus
    CampusName = models.CharField(max_length=60, default="", blank=True, null=False) #Attribute with character field, blank=True mean it can be blank, null=False means it will not accept a null value.
    State = models.CharField(max_length=2, default="", blank=True, null=False)
    CampusID = models.IntegerField(default="", blank=True, null=False)
    #names model manager 'object'
    object = models.Manager()

    def __str__(self):
        # Returns the input value of the CampusName to display in the browser instead of the default titles
        return self.CampusName

    class Meta:
        #tells browser window to display this value instead of adding an 's' for plural
        verbose_name_plural = "University Campus"