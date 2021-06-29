from rest_framework import serializers
from .models import *

class DaySerializer(serializers.ModelSerializer):

    class Meta:
        model=Day
        fields='__all__'


