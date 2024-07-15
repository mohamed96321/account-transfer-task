from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
import csv
from .models import Account
from .serializers import AccountSerializer
from io import StringIO

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @action(detail=False, methods=['post'])
    def import_accounts(self, request):
        file = request.FILES['file']
        decoded_file = file.read().decode('utf-8')
        io_string = StringIO(decoded_file)
        reader = csv.DictReader(io_string)

        for row in reader:
            Account.objects.create(
                id=row['ID'],
                name=row['Name'],
                balance=row['Balance']
            )
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def transfer(self, request, pk=None):
        from_account = get_object_or_404(Account, pk=pk)
        to_account = get_object_or_404(Account, pk=request.data['to_account_id'])
        amount = float(request.data['amount'])

        if from_account.balance >= amount:
            from_account.balance -= amount
            to_account.balance += amount
            from_account.save()
            to_account.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)
