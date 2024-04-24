from rest_framework import generics
from .models import Test, Question, Answer
from .serializers import TestSerializer, QuestionSerializer, AnswerSerializer

class TestList(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestDetail(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class QuestionDetail(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerDetail(generics.RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
