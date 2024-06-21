from django.db import models
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User

class New(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	text = models.TextField()
	data = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

class Race(models.Model):
	name = models.CharField(max_length=50, db_index=True)
	age = models.CharField(max_length=30)
	size = models.CharField(max_length=30)	
	speed = models.CharField(max_length=30)
	languages = models.CharField(max_length=30)
	subraces = models.CharField(max_length=30)
	desc = models.TextField()
	img = models.ImageField(null = True, blank = True, upload_to = "static/img/")

class Class(models.Model):
	name = models.CharField(max_length=50, db_index=True)
	desc = models.TextField()
	ability = models.CharField(max_length=50)
	armor_weapon = models.CharField(max_length=50)
	img = models.ImageField(null = True, blank = True, upload_to = "static/img/")

class Dialogue(models.Model):
	ud = models.ForeignKey('User_dialogues', on_delete = models.CASCADE)
	
	user_input = models.TextField()
	ai_output = models.TextField()
	ai_img = models.ImageField(null = True, blank = True, upload_to = "static/img/")

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	bio = models.TextField(null=True, blank=True)
	profile_pic = models.ImageField(null=True, blank=True, upload_to="static/img/profile")
	location = models.CharField(max_length=30, null=True, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	def __str__(self):
		return self.user.username


class User_dialogues(models.Model):
	u = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=30, null = True, blank=True)
	character_name = models.CharField(max_length=30)
	character_background = models.CharField(max_length=500, null = True, blank=True)
	setting = models.TextField()
	img = models.ImageField(null = True, blank = True, upload_to = "static/img/")
	
	history = models.TextField(null = True, blank = True)

class Monster(models.Model):
	name = models.CharField(max_length=50, db_index=True)
	speed = models.CharField(max_length=50)
	strength = models.CharField(max_length=50)
	wisdom = models.CharField(max_length=50)
	charisma = models.CharField(max_length=50)
	dexterity = models.CharField(max_length=50)
	constitution = models.CharField(max_length=50)
	intelligence = models.CharField(max_length=50)
	danger = models.CharField(max_length=50)
	languages = models.TextField()
	senses = models.TextField()
	armor_class = models.TextField()
	desc = models.TextField()

	img = models.ImageField(null = True, blank = True, upload_to = "static/img/")
