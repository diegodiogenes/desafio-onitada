from rest_framework import serializers
from .models import Payment
from loans.models import Loan
from loans.serializers import LoanSerializer


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ['loan', 'payment_date', 'value']
        extra_kwargs = {'payment_date': {'read_only': True}}

    def validate_loan(self, value: Loan) -> Loan:
        request = self.context.get("request")

        if value.client != request.user:
            message = 'You don\'t have permission to access this Loan'
            raise serializers.ValidationError(message)
        return value
