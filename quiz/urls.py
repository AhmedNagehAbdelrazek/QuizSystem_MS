from django.urls import path
from .views import (
    QuestionListCreate, QuestionRetrieveUpdateDestroy,
    QuizListCreate, QuizRetrieveUpdateDestroy,
    ApplicationListCreate, ApplicationRetrieveUpdateDestroy,
    AnswerListCreate, AnswerRetrieveUpdateDestroy
)

urlpatterns = [
    path('questions/', QuestionListCreate.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', QuestionRetrieveUpdateDestroy.as_view(), name='question-detail'),
    
    path('quizzes/', QuizListCreate.as_view(), name='quiz-list-create'),
    path('quizzes/<int:pk>/', QuizRetrieveUpdateDestroy.as_view(), name='quiz-detail'),
    
    path('applications/', ApplicationListCreate.as_view(), name='application-list-create'),
    path('applications/<int:pk>/', ApplicationRetrieveUpdateDestroy.as_view(), name='application-detail'),
    
    path('answers/', AnswerListCreate.as_view(), name='answer-list-create'),
    path('answers/<int:pk>/', AnswerRetrieveUpdateDestroy.as_view(), name='answer-detail'),
]