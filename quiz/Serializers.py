from rest_framework import serializers
from django.contrib.auth.models import User
from  .models import *

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    questions = QuizQuestionSerializer(source='quizquestion_set', many=True, read_only=True)
    
    class Meta:
        model = Quiz
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'