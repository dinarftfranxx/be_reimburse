from rest_framework import serializers
from .categorySerializer import CategorySerializers
from api.models import ReimbursementItems

class ReimbursementItemSerializers(serializers.ModelSerializer):
    category = CategorySerializers(read_only=True)
    class Meta:
        model = ReimbursementItems
        fields = [
            'id',
            # 'reimbursement',
            'category',
            'item_amount',
            'created_at',
            'updated_at'
        ]