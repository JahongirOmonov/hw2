from rest_framework.serializers import ModelSerializer
from .models import Korxona

class KorxonaSerializer(ModelSerializer):
    class Meta:
        model = Korxona
        fields=('__all__')