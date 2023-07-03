from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django.shortcuts import render
from django.forms import model_to_dict
from .models import *
from .serializers import UfsstarsSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly



class UfcstarsViewSet(viewsets.ModelViewSet):
    queryset = Ufsstars.objects.all()
    serializer_class = UfsstarsSerializer

    def queryset_get(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Ufsstars.objects.all()

        return Ufsstars.objects.filter(pk=pk)

    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #
    #     if not pk:
    #         return Ufsstars.objects.all()[:3]
    #
    #     return Ufsstars.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        arts = Art.objects.get(pk=pk)
        return Response({'arts': arts.type_of_art})


class UfcstarsAPIView(generics.ListAPIView):
    queryset = Ufsstars.objects.all()
    serializer_class = UfsstarsSerializer

class UfcstarAPIList(generics.ListCreateAPIView):
    queryset = Ufsstars.objects.all()
    serializer_class = UfsstarsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class UfcstarAPIupdate(generics.RetrieveUpdateAPIView):
    queryset = Ufsstars.objects.all()
    serializer_class = UfsstarsSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class UfcCRUD(generics.RetrieveDestroyAPIView):
    queryset = Ufsstars.objects.all()
    serializer_class = UfsstarsSerializer
    permission_classes = (IsAdminOrReadOnly,)

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

