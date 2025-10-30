from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True},
             'email': {'required': True} # 'write_only' artinya password tidak akan
                                             # dikirim balik di respon (biar aman)
        }

    def create(self, validated_data):
        # Kita pakai create_user agar password-nya di-hash (dienkripsi)
        # BUKAN disimpan sebagai teks biasa. Ini WAJIB!
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
    # def validate_username(self, value):
    #     if User.objects.filter(username=value).exists():
    #         raise serializers.ValidationError("username udah ada")
    #     return
    # ini tidak usah karena sudah ada darisananya
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("email udah ada")
        return
    
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


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'created_at'
        ]

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
    