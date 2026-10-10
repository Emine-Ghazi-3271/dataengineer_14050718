from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def deployment_sample(request):
    return HttpResponse("Hello, world. You're at the deployment sample.")

