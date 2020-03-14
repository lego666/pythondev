from django.shortcuts import render

def index(request):
	return render(request, 'mainApp/homePage.html')

def contact(request):
	return render(request, 'mainApp/basic.html', {'values': ['Если у Вас есть вопросы, звоните :)', '999-999-9']})