from django.shortcuts import render
from rest_framework import viewsets
from .models import PDocs
from .serializers import PDocsSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class PDocViewSet(viewsets.ModelViewSet):
    serializer_class = PDocsSerializer
    queryset = PDocs.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return PDocs.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
