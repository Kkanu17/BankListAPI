from rest_framework import serializers
from .models import Branch , Bank


class BranchesSerializer(serializers.HyperlinkedModelSerializer):
    
    bank_name = serializers.CharField(source='bank_id.name')
    class Meta:
        model = Branch
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer):
        class Meta:
             model= Bank
             fields = '__all__'