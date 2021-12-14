from rest_framework import serializers
from .models import employs
class empSerel(serializers.ModelSerializer):
    class Meta:
        model = employs
        fields = ('firstname','lastname')