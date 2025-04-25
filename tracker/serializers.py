from rest_framework import serializers
from django.contrib.auth.models import User
from tracker.models import Expense,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ['id', 'name']

class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
   
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

    class Meta:
        model = Expense
        fields = ['id', 'title', 'amount', 'date', 'category', 'category_id']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['username','password']

    def create(self,validated_data):
        user=User.objects.create_user(username=validated_data['username'],
                                      password=validated_data['password'])
        return user