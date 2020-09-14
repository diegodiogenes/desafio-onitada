from django.db import models
from loans.models import Loan


# Create your models here.
class Payment(models.Model):
    """
    Payment Model
    """
    # foreign keys
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='payments', help_text='Related Loan')
    # fields
    payment_date = models.DateTimeField(auto_now_add=True, editable=False, help_text='Payment date')
    value = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name="Payment Value",
                                help_text="Payment Value to the Loan")
