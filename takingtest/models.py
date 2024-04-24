from django.db import models
from account.models import CustomUser
from testing.models import Test,Question,Answer


class TestTaking(models.Model):
    user = models.ForeignKey(CustomUser, related_name='test_takings', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name='test_takings', on_delete=models.CASCADE)
    taking_question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    user_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.test.title}"