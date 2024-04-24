from rest_framework import serializers
from .models import TestTaking

class TestTakingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTaking
        fields = ['id', 'user', 'test', 'taking_question', 'completed']