from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
def home(r):
    return render(r, 'base.html')


@api_view(["POST"])
def create_key(r):
    print(r.data["logs"])
    k = Key.objects.create(key=r.data.get('logs')
)
    k.save()
    return Response({"msg":"success"})
