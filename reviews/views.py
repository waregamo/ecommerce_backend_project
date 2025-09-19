from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import AllowAny

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]  # anyone can view

    # Optional: filtering, search, ordering
    filterset_fields = ["product", "user", "rating"]
    search_fields = ["comment"]
    ordering_fields = ["created_at", "rating"]
    ordering = ["-created_at"]