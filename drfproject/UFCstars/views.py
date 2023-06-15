from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.forms import model_to_dict
from .models import *
from .serializers import UfsstarsSerializer

class UfcstarsAPIView(generics.ListAPIView):
    queryset = Ufsstars.objects.all()
    serializer_class = UfsstarsSerializer


class UfcstarAPIView(APIView):

    def get(self, request):
        list1 = Ufsstars.objects.all().values()
        return Response({'Fighters': list(list1)})

    def post(self, request):
        new_post = Ufsstars.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            art_id=request.data['art_id'],
            weight_id=request.data['weight_id']
        )

        return Response({'post': model_to_dict(new_post)})