from django.db import models

class Customer(models.Model):
	#primary
	customerID = models.AutoField(primary_key=True)
	##--------------------------------------------------------
	username = models.CharField(max_length=50, unique=True)
        password = models.CharField(max_length=50)
        ##--------------------------------------------------------
	lastName = models.CharField(max_length=50)
	firstName = models.CharField(max_length=50)
	email = models.EmailField()
	diet = models.ForeignKey(Diet, to_field='dietID', on_delete=models.PROTECT) 

class Shipping(models.Model):
	#primary	
	shippingID = models.AutoField(primary_key=True)
	##--------------------------------------------------------
	customerID = models.ForeignKey(Customer, to_field='customerID', on_delete=models.PROTECT)
	##--------------------------------------------------------
	phoneNum = models.CharField(max_length=12, blank=True)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state = models.CharField(max_length=20)
	zipCode = models.PositiveIntegerField()

class Billing(models.Model):
	#primary
	billingID = models.AutoField(primary_key=True)
	##--------------------------------------------------------
	customerID = models.ForeignKey(Customer, to_field='customerID', on_delete=models.PROTECT)
	paymentAmount = models.CharField(max_length=7)
	paypalEmailAccount = models.EmailField()

class Employee(models.Model):
	#primary
	employeeID = models.AutoField(primary_key=True)
	#--------------------------------------------------------
	position = models.CharField(max_length=50)
	isAdmin = models.BooleanField(default=False)
	lastName = models.CharField(max_length=50)
	firstName = models.CharField(max_length=50)
	phone = models.CharField(max_length=12)
	username = models.CharField(max_length=50, unique=True)
	password = models.CharField(max_length=50)
	wage = models.PositiveIntegerField()

class Meal(models.Model):
	#primary
	mealID = models.AutoField(primary_key=True)
	dishName = models.CharField(max_length=50, unique=True)
	substitution1 = models.CharField(max_length=50)
	substituiotn2 = models.CharField(max_length=50)
        diet = models.ForeignKey(Diet, to_field='dietID', on_delete=models.PROTECT)
	
class Order(models.Model):
	#primary
	orderID = models.AutoField(primary_key=True)
	#--------------------------------------------------------
	customerID = models.ForeignKey(Customer, to_field='customerID', on_delete=models.PROTECT)
	#--------------------------------------------------------
	empID = models.ForeignKey(Employee, to_field='empID', on_delete=models.PROTECT)
	orderDate = models.DateTimeField(auto_now_add=True)
	#all meals are FKs and instances of class Meal

class Diet(models.Model):
        #primary
        dietID = models.AutoField(primary_key=True)
        dietName = models.CharField(max_length=50)

        keto = models.BooleanField(default=False)
        glutenFree = models.BooleanField(default=False)
        vegan = models.BooleanField(default=False)
        vegitarian = models.BooleanField(default=False)
        highProtein = models.BooleanField(default=False)


