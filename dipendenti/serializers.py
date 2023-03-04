from .models import Dipendenti
from rest_framework import serializers

class DipendentiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dipendenti
        fields = ['id', 'name', 'email', 'job_title', 'phone', 'employee_code']
