from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 40) 

    class Meta:
        db_table= "menu"	

class Category(models.Model):
    menu = models.ForeignKey("Menu",on_delete=models.CASCADE)		# Menu클래스에 연결 
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = "category"

class Nutrition(models.Model):
    kcal	 = models.DecimalField(max_digits = 6, decimal_places = 2)
    sodium   = models.DecimalField(max_digits = 6, decimal_places = 2)	# 6자리, 소숫점은 2자리까지
    sugars   = models.DecimalField(max_digits = 6, decimal_places = 2)
    protein  = models.DecimalField(max_digits = 6, decimal_places = 2)
    caffeine = models.DecimalField(max_digits = 6, decimal_places = 2)

    class Meta:
        db_table = "nutrition"

class Drink(models.Model):
    category    = models.ForeignKey("Category", on_delete=models.CASCADE)	# Category 클래스에 연결 
    nutrition   = models.ForeignKey("Nutrition", on_delete=models.CASCADE)	# Nutrition 클래스에 연결 
    name        = models.CharField(max_length = 45)
    allergy     = models.ManyToManyField("Allergy", through = "Allergy_Drink")	# "through="Allergy_Drink"는 many to many 거는 법 !  

    class Meta:
        db_table = "drink"

class Allergy(models.Model):
    name = models.CharField(max_length= 45)

    class Meta:
        db_table = "allergy"

class Allergy_Drink(models.Model):
    drink = models.ForeignKey("Drink", on_delete=models.CASCADE)		   # Drink 클래스에 연결 
    allergy = models.ForeignKey("Allergy", on_delete=models.CASCADE, null = True)  # Allergy 클래스에 연결

    class Meta:
        db_table = "allergy_drink"