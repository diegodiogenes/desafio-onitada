from rest_framework import status
from rest_framework.test import APITestCase
from .models import Loan
from rest_framework.authtoken.models import Token
from django.urls import reverse


# Create your tests here.
class LoanTestCase(APITestCase):
    fixtures = ['users.json', 'loans.json']

    def setUp(self) -> None:
        token = Token.objects.get(user__username="johnlennon")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.valid_payload = {
            "value": "2000.00",
            "interest_value": "0.008",
            "bank": "Itau Unibanco"
        }

    def test_create_valid_loan(self) -> None:
        response = self.client.post('/api/loans/',
                                    data=self.valid_payload,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_loan(self) -> None:
        loan = Loan.objects.filter(client__username="johnlennon").first()

        response = self.client.get(self.reverse_url('loans-detail', pk=loan.pk))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_updatet_loan(self) -> None:
        loan = Loan.objects.filter(client__username="johnlennon").first()

        response = self.client.put(self.reverse_url('loans-detail', pk=loan.pk), data={'bank': 'Banco Santander'},
                                   format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_loan_another_client(self) -> None:
        loan = Loan.objects.filter(client__username="paulmc").first()

        response = self.client.get(self.reverse_url('loans-detail', pk=loan.pk))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def reverse_url(self, name, **kwargs) -> str:
        url = reverse(name, kwargs=kwargs)
        return url
