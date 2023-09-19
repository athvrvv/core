from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    peoples=[
        {'name':'abhijeet','age':26},
        {'name':'vicky','age':24}
    ] 
    for people in peoples:
        print(people)






    return render(request ,"index.html",context={'peoples':peoples})
def success_page(request):
    print("*"*10)
    return HttpResponse("<h1>hey this is a success page</h1>")