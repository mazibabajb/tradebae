from django.db import models

# Create your models here.
BODYTYPE_CHOICES = (
     ('Single-cab', 'Single-cab'),
     ('double-cab', 'double-cab'),
     ('sedan', 'sedan'),
     ('hatchback', 'hatchback'),
     ('truck', 'truck'),
     ('suv', 'suv'),
     ('Any', 'Any')
	)

FUEL_CHOICES = (
     ('petrol', 'petrol'),
     ('deasel', 'diesel'),
     
	)

TRANSMITION_CHOICES = (
     ('manual', 'manual'),
     ('automatic', 'automatic'),
     
	)
ACCESS_CHOICES = (
     ('YES', 'YES'),
     ('NO', 'NO'),
     
	)
CAR_CHOICES = (
     ('CAR', 'CAR'),
     ('Mazda', 'Mazda'),
     ('Ford', 'Ford'),
     ('Nissan', 'Nissan'),
     ('Toyota', 'Toyota'),
     ('Bmw', 'Bmw'),
     ('Audi', 'Audi'),
     ('Mercedes benz', 'Mercedes benz'),
     ('Vw', 'Vw'),
     ('Honda', 'Honda'),
     ('Pegeot', 'Pegeot'),
     ('Pocshe', 'Posche'),
     
	)


class Contact_us(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    created_with = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.firstname} Contact'

class owner(models.Model):
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	Addresses = models.CharField(max_length=30)
	cell_mobile_phone = models.CharField(max_length=30)
	Whatsapp_number = models.CharField(max_length=30)
	optionai_contact = models.CharField(max_length=30)


class Car(models.Model):
	car_id = models.AutoField(primary_key=True)
	seller = models.ForeignKey(owner, on_delete=models.CASCADE)
	make = models.CharField(
        choices=CAR_CHOICES,
        default='car',
        max_length=30)

	model = models.CharField(max_length=30)
	fuel_type = models.CharField(
        choices= FUEL_CHOICES,
        default='petrol',
        max_length=30)
	engine_size = models.CharField(max_length=30)
	year_of_use = models.CharField(max_length=30)
	year_of_manufacture = models.CharField(max_length=30)
	body_type = models.CharField(
        choices=BODYTYPE_CHOICES,
        default='any',
        max_length=30)
	transmition = models.CharField(
        choices=TRANSMITION_CHOICES,
        default='manual',
        max_length=30)
	millage = models.CharField(max_length=30)
	price = models.CharField(max_length=30)
	dscription = models.CharField(max_length=300)
	created_with = models.DateTimeField(auto_now=True)
	car_img = models.ImageField(default='default.png',upload_to='profile_pics')
	air_conditioner = models.CharField(
        choices=ACCESS_CHOICES,
        default='yes',
        max_length=30)
	power_steering = models.CharField(
        choices=ACCESS_CHOICES,
        default='yes',
        max_length=30)
	cd_Player = models.CharField(
        choices=ACCESS_CHOICES,
        default='yes',
        max_length=30)
	brake_assist = models.CharField(
        choices=ACCESS_CHOICES,
        default='yes',
        max_length=30)
	antilock_braking_system = models.CharField(
        choices=ACCESS_CHOICES,
        default='yes',
        max_length=30)
	power_windows = models.CharField(
        choices=ACCESS_CHOICES,
        default='yes',
        max_length=30)
	leather_seats = models.CharField(
        choices=ACCESS_CHOICES,
        default='yes',
        max_length=30)
	power_door_locks = models.CharField(
        choices=ACCESS_CHOICES,
        default='yes',
        max_length=30)
	driver_airbag = models.CharField(
        choices=ACCESS_CHOICES,
        default='yes',
        max_length=30)
	central_locking= models.CharField(
        choices=ACCESS_CHOICES,
        default='yes',
        max_length=30)
	fog_lamps = models.CharField(
        choices=ACCESS_CHOICES,
        default='yes',
        max_length=30)

	def __str__(self):
		return self.make
		







class phone(models.Model):
	phone_id = models.AutoField(primary_key=True)
	seller = models.ForeignKey(owner, on_delete=models.CASCADE)
	brand = models.CharField(max_length=30)
	model = models.CharField(max_length=30)
	price = models.CharField(max_length=30)
	ram = models.CharField(max_length=30)
	storage = models.CharField(max_length=30)	