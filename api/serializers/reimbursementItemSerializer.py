from rest_framework import serializers
from .reimbursementSerializer import ReimbursementSerializers
from .categorySerializer import CategorySerializers
from api.models import ReimbursementItems

class ReimbursementItemSerializers(serializers.ModelSerializer):
    reimbursement = ReimbursementSerializers(read_only=True)
    category = CategorySerializers(read_only=True)
    class Meta:
        model = ReimbursementItems
        fields = [
            'id',
            'reimbursement',
            'category',
            'item_amount',
            'created_at',
            'updated_at'
        ]