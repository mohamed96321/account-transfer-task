from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Account

class AccountTests(APITestCase):
    def setUp(self):
        self.account1 = Account.objects.create(id='cc26b56c-36f6-41f1-b689-d1d5065b95af', name='Joy Dean', balance=4497.22)
        self.account2 = Account.objects.create(id='be6acfdc-cae1-4611-b3b2-dfb5167ba5fe', name='Bryan Rice', balance=2632.76)
        self.account3 = Account.objects.create(id='43caa0b8-76a4-4e61-b7c3-f2f5ee4b4f77', name='Ms. Jamie Lopez', balance=1827.85)

    def test_list_accounts(self):
        url = reverse('account-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_account(self):
        url = reverse('account-detail', args=[self.account1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_transfer_funds(self):
        url = reverse('account-transfer', args=[self.account1.id])
        data = {'to_account_id': self.account2.id, 'amount': 1000}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.account1.refresh_from_db()
        self.account2.refresh_from_db()

        self.assertEqual(self.account1.balance, 3497.22)
        self.assertEqual(self.account2.balance, 3632.76)
