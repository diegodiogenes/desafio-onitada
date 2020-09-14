from django.db import models
from users.models import User
from django.db.models import Sum
import pytz
import datetime
from decimal import Decimal
import uuid, json


# Create your models here.
class Loan(models.Model):
    """
    Loan Model
    """
    # foreign keys
    client = models.ForeignKey(User, related_name='loans', on_delete=models.CASCADE, help_text='Loan Client')
    # fields
    value = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name="Value of Bank Loan",
                                help_text="Value owed to the Bank Loan")
    interest_value = models.DecimalField(default=0.000, max_digits=6, decimal_places=3,
                                         verbose_name="Monthly Interest Rate", help_text="Monthly Interest Rate")
    ip_address = models.GenericIPAddressField(verbose_name='Ip address',
                                              help_text='Ip address of the contract submitter')
    bank = models.TextField(verbose_name="Bank of Loan", help_text='Informations about the Bank of Loan')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, help_text='Loan creation date')

    # meta
    class Meta:
        ordering = ['id']

    # functions
    def __str__(self):
        return "R$ {}, {}".format(self.value, self.bank)

    def get_elapsed_time(self) -> int:
        """
        Returns the elapsed time of the loan
        """
        today = datetime.datetime.now(pytz.utc)
        loan_date = self.created_at

        return (today - loan_date).days

    @property
    def balance(self) -> float:
        """
        Returns the balance of the loan
        """
        return round(self.amount + self.iof - self.paid_value, 2)

    @property
    def amount(self) -> Decimal:
        """
        Calculate the amount pro rata die of the loan by compound interest
        """
        pro_rata = round(self.interest_value / 30, 3)

        elapsed_time = self.get_elapsed_time()

        return self.value + ((1 + pro_rata) ** elapsed_time)

    @property
    def iof(self) -> Decimal:
        """
        Calculate the loan tax IOF
        """
        aliquot = self.value * Decimal(0.38 / 100.0)

        aliquot_days = self.get_elapsed_time() * Decimal(0.0082 / 100.0) * self.value

        return round(aliquot + aliquot_days, 2)

    @property
    def paid_value(self) -> Decimal:
        """
        Returns the paid value
        """
        return self.payments.aggregate(Sum('value')).get('value__sum') or Decimal(0.00)
