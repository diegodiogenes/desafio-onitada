from .models import Payment
from .serializers import *
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer

    def get_queryset(self) -> object:
        return Payment.objects.filter(loan__client=self.request.user)
