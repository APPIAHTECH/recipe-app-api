from core.models import Ingredient
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for an ingredient object"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)