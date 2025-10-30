from rest_framework import serializers
from api.models import Reimbursement
from .userSerializer import UserSerializers
from .reimbursementItemSerializer import ReimbursementItemSerializers

class ReimbursementSerializers(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    items = ReimbursementItemSerializers(source='reimbursementitems_set', many=True, read_only=True)
    class Meta:
        model = Reimbursement
        fields = [
            'id',
            'user',
            'title',
            'total_amount',
            'created_at',
            'updated_at',
            'description',
            'image',
            'status',
            'items'
        ]