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
        w = Ufsstars.objects.all()
        return Response({'Fighters': UfsstarsSerializer(w, many=True).data})

    def post(self, request):
        serializer = UfsstarsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Ufsstars.objects.get(pk=pk)
        except:
            return Response({"error":"Object does not exist"})

        serializer = UfsstarsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            instance = Ufsstars.objects.get(pk=pk)
            instance.delete()
        except:
            Response({"error":"Object does not exist"})

        return Response({"post":"delete post" + str(pk)})

