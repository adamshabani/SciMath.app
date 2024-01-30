from django.shortcuts import render
from rest_framework import generics
from .serializers import QuizSerializer,RandomQuestionSerializer,QuizQuestionSerializer
from rest_framework.response import Response
from .models import Quizzes,Questions,Answers
from rest_framework.views import APIView


# Create your views here.


class Quiz(generics.ListAPIView):
    
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all() 
    
    
    
class RandomQuestion(APIView):
    
    def get(self, request, format=None, **kwargs):
        question = Questions.objects.filter(quiz__title=kwargs['topics']). order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):
    
    def get(self, request, format=None, **kwargs):
        question = Questions.objects.filter(quiz__title=kwargs['topics'])
        serializer = QuizQuestionSerializer(question, many=True, read_only=True)
        return Response(serializer.data)
