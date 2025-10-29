from rest_framework import serializers
from api.models import Reimbursement
from .userSerializer import UserSerializer

class ReimbursementSerializers(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Reimbursement
        fields = [
            'id',
            'user',
            'title',
            'amount',
            'created_at',
            'updated_at',
            'description',
            'image',
            'status'
        ]