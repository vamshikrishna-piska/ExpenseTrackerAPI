from rest_framework import viewsets, permissions,generics
from django.contrib.auth.models import User
from tracker.models import Expense, Category
from tracker.serializers import ExpenseSerializer, CategorySerializer,UserRegistrationSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class UserRegistrationView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserRegistrationSerializer


