from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .models import Loan
from ipware import get_client_ip


# Create your views here.
class LoanViewSet(ModelViewSet):
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Loan.objects.filter(client=self.request.user)

    def perform_create(self, serializer):
        client_ip, _ = get_client_ip(self.request)
        serializer.save(client=self.request.user, ip_address=client_ip)
