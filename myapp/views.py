from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student

# Create your views here.

class StudentCreate(CreateView):
	model=Student
	fields=['name', 'mark']
