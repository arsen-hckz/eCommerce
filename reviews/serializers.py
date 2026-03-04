from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Review
        fields = ["id", "user_email", "product", "rating", "comment", "created_at"]
        read_only_fields = ["id", "user_email", "created_at"]

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5")
        return value

    def validate(self, attrs):
        request = self.context.get("request")
        product = attrs.get("product")
        if request and Review.objects.filter(user=request.user, product=product).exists():
            raise serializers.ValidationError("You have already reviewed this product")
        return attrs