# File: api/views/reimbursementView.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.serializers import ReimbursementSerializers # Impor dari "bos" serializer
from api.models import Reimbursement # Impor dari "bos" models

class ReimbursementListView(generics.ListAPIView):
    serializer_class = ReimbursementSerializers # Pakai resep plural
    permission_classes = [IsAuthenticated] # Wajib login
    
    def get_queryset(self):
        # Cuma tampilkan data milik user yang sedang login
        # dan urutkan dari yang paling baru
        return Reimbursement.objects.filter(user=self.request.user).order_by('-created_at')