from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = ['id', 'value', 'interest_value', 'bank', 'created_at', 'amount', 'iof', 'paid_value', 'balance']
        read_only_fields = ['created_at', 'client', 'ip_address', 'balance']
