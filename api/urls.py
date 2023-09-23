from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CustomUserViewSet, CategoryViewSet, ProductViewSet, OrderViewSet, OrderItemViewSet, ProfileUpdateView


router = SimpleRouter()
router.register('users', CustomUserViewSet, basename='customeruser')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'item', OrderItemViewSet, basename='order item')


urlpatterns =[
    path('update/', ProfileUpdateView.as_view(), name='profile'),
] + router.urls 