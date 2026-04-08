from rest_framework import serializers
from .models import LearningEntry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningEntry
        fields = '__all__'