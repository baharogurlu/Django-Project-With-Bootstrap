from django.db import models

# Create your models here.
class Question(models.Model):
 question_text=models.CharField(max_length=200)
 pub_date=models.DateField('date published')

 def __str__(self):
  return self.question_text

class Choice(models.Model):
 choice_text=models.TextField()
 vote=models.IntegerField(default=0)
 question=models.ForeignKey(Question,on_delete=models.CASCADE)

 def __str__(self):
  return self.choice_text