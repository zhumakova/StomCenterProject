from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import *

class DayViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class=DaySerializer

    def list(self,request):
        days=Day.objects.all()
        serializer=self.serializer_class(days,many=True)
        return Response(serializer.data)