from django.urls import path
from .views import PaymentListCreateView, PaymentDetailView

urlpatterns = [
    path("", PaymentListCreateView.as_view(), name="payment-list-create"),
    path("<int:pk>/", PaymentDetailView.as_view(), name="payment-detail"),
]
