import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Quiz(models.Model):
	quiz_description = models.CharField(max_length = 400)
	good_answer = models.CharField(max_length=400)
	create_date = models.DateTimeField("Create Date", auto_now = True)

	def __str__(self):
		return self.quiz_description

	def was_published_recently(self):
		return self.create_date >= timezone.now() - datetime.timedelta(days=1)

class estudiantes(models.Model):
	est_name = models.CharField(max_length = 500)
	email = models.CharField(max_length=500)


class submition(models.Model):
	quizID = models.ForeignKey(Quiz, on_delete = models.CASCADE)
	estID = models.ForeignKey(estudiantes, on_delete = models.CASCADE)
	result = models.IntegerField(default = 0 )
	submit_date = models.DateTimeField("date submit",  auto_now = True	)

	

class keys(models.Model):
	quizID = models.ForeignKey(Quiz, on_delete = models.CASCADE)
	estID = models.ForeignKey(estudiantes, on_delete= models.CASCADE)
	key_i = models.CharField(max_length = 15)

	def __str__(self):
		return self.key_i

