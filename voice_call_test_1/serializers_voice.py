from rest_framework import serializers 
from .models import voice_call_array

class serializers_voice_call_test(serializers.ModelSerializer):
    class Meta:
        model=voice_call_array
        fields=('sender_number','receiver_numer','voice_array')