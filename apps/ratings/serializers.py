from rest_framework import serializers
from.models import Rating

class RatingSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        models = Rating
        exclude = ["updated_at", "pkid",]

    def get_customer(self, obj):
        return obj.customer.username
    
    def get_agent(self, obj):
        return obj.agent.user.username