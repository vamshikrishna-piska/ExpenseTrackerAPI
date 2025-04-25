from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tracker.views import ExpenseViewSet, CategoryViewSet,UserRegistrationView

router = DefaultRouter()
router.register('expenses', ExpenseViewSet, basename='expense')
router.register('categories', CategoryViewSet, basename='category')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user_register'),
]
