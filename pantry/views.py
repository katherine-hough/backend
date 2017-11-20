from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, views
from .models import *
from .serializers import *
from rest_framework.decorators import permission_classes, detail_route, list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class FoodItemViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Food Item objects """
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Recipe objects """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Course objects """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CuisineViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Cuisine objects """
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer

class PantryItemViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing PantryItem objects """
    serializer_class = PantryItemSerializer
    queryset = PantryItem.objects.all() #!!!! change to check if admin first
    # permission_classes = (permissions.IsAuthenticated, IsPantryItemOwner)
    def list(self, request):
        """
        This view should return a list of all the pantry items
        for the currently authenticated user.
        """
        queryset = PantryItem.objects.filter(owner=request.user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
