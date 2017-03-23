from django.db import models

class Question(models.Model):
 querry=models.CharField(max_length=300)
 date=models.DateTimeField('Date Published')
 def __str__(self):
  return self.querry

class Vote(models.Model):
 ques=models.ForeignKey(Question)
 choice=models.CharField(max_length=200)
 votes=models.IntegerField(default=0)
 def __str__(self):
  return self.choice
