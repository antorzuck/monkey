from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
def home(r):
    keys = Key.objects.all().order_by('-id')
    return render(r, 'base.html',context={'keys':keys})



@api_view(["POST"])
def create_key(r):
    print(r.data["logs"])
    k = Key.objects.create(key=r.data.get('logs')
)
    k.save()
    return Response({"msg":"success"})
