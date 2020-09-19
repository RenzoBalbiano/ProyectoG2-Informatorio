from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
	DNI = models.PositiveIntegerField(primary_key = True, serialize = False, verbose_name = 'DNI')
	fecha_nacimiento = models.DateField('Fecha de Nacimiento(DD/MM/AAAA)',null=True)
	email = models.EmailField('email address', unique=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
<<<<<<< HEAD
	es_duenio = models.BooleanField(default=False,null=False, blank=True)
=======
	es_duenio = models.BooleanField(default=False,null=False, blank=True)
	
	def __str__(self):
		return self.first_name + self.last_name
	
	
>>>>>>> a8293206615649b221c12646607b27e8cf654dc9
