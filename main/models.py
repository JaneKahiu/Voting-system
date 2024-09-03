from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
  
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'choice')

    def __str__(self):
        return f"{self.user.username} voted for {self.choice.choice_text}"

