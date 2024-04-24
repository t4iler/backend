from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
    
class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self) -> str:
        return self.question
    
class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=50)
    answer_explanation = models.CharField(max_length=200, blank=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer