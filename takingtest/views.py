from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import TestTaking
from testing.models import Answer
from testing.serializers import QuestionSerializer
from .serializers import TestTakingSerializer

class CustomPagination(PageNumberPagination):
    page_size = 1  
    page_size_query_param = 'page_size'
    max_page_size = 1 

class TestTakingList(APIView):
    def get(self, request):
        test_takings = TestTaking.objects.all()
        serializer = TestTakingSerializer(test_takings, many=True)
        return Response(serializer.data)

class StartTest(APIView):
    def post(self, request):
        test_id = request.data.get('test_id')
        user_id = request.data.get('user_id')
        if not test_id or not user_id:
            return Response({'error': 'Test ID and User ID are required'}, status=status.HTTP_400_BAD_REQUEST)
        test_taking = TestTaking.objects.create(user_id=user_id, test_id=test_id)
        return Response({'test_taking_id': test_taking.id}, status=status.HTTP_201_CREATED)
    

class DisplayQuestion(APIView):
    def get(self, request, test_taking_id):
        try:
            test_taking = TestTaking.objects.get(id=test_taking_id)
        except TestTaking.DoesNotExist:
            return Response({'error': 'TestTaking not found'}, status=status.HTTP_404_NOT_FOUND)
        taking_question = test_taking.test.questions.first()
        if test_taking.taking_question:
            next_question = test_taking.test.questions.filter(id__gt=test_taking.taking_question.id).first()
            if next_question:
                taking_question = next_question
        test_taking.taking_question = taking_question
        test_taking.save()
        serialized_question = QuestionSerializer(taking_question)
        return Response(serialized_question.data, status=status.HTTP_200_OK)


class FinishTest(APIView):
    def put(self, request, test_taking_id):
        try:
            test_taking = TestTaking.objects.get(id=test_taking_id)
        except TestTaking.DoesNotExist:
            return Response({'error': 'TestTaking not found'}, status=status.HTTP_404_NOT_FOUND)
        test_taking.completed = True
        test_taking.save()
        return Response({'message': 'Test completed'}, status=status.HTTP_200_OK)
    
class SubmitAnswer(APIView):
    def post(self, request, test_taking_id):
        answer_id = request.data.get('answer_id')

        try:
            test_taking = TestTaking.objects.get(id=test_taking_id)
            answer = Answer.objects.get(id=answer_id)
        except TestTaking.DoesNotExist:
            return Response({'error': 'TestTaking not found'}, status=status.HTTP_404_NOT_FOUND)
        except Answer.DoesNotExist:
            return Response({'error': 'Answer not found'}, status=status.HTTP_404_NOT_FOUND)
        test_taking.user_answer = answer
        test_taking.save()
        result = 'correct' if answer.is_correct else 'incorrect'
        return Response({'result': result}, status=status.HTTP_200_OK)
