from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import BranchesSerializer,BankSerializer
from rest_framework.decorators import action
from .models import Bank, Branch

# ViewSet for bank Table is created 

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
       
# ViewSet for Branch Table is created along with getting the Bank List and its branch details for a specific branch.

class BranchesViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchesSerializer
    def get_queryset(self):
        branch_name = self.request.query_params.get('branch')
        qs = Branch.objects.all()
        if branch_name is not None:
            qs = qs.filter(branch = branch_name.upper())
        
        return qs
   