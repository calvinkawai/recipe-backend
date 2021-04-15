from rest_framework import serializers
from recipe.models import Recipe
from django.contrib.auth.models import User

class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Recipe
        fields = ["id", "name", "ingredient", "steps", "image", "owner"]

class UserSerializer(serializers.ModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'recipe']
