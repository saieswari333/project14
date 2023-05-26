from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    res=HttpResponse("""<html><body bgcolor=bloue><h1><center>welcome to django project1</center></h1></body</html>""")
    return res


