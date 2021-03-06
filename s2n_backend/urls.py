"""s2n_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import (url, include)
from rest_framework import routers
from django.contrib import admin
from pantry.views import *

pantry_bindings = PantryItemViewSet.as_view({
    'get': 'list',
    'post': 'put',
    'delete': 'delete',
})

favorites_bindings = FavoriteRecipeViewSet.as_view({
    'get': 'list',
    'post': 'put',
    'delete': 'delete',
})

router = routers.DefaultRouter()
router.register(prefix='api/foods', viewset=FoodItemViewSet)
router.register(prefix='api/recipes', viewset=RecipeViewSet)
router.register(prefix='api/cuisines', viewset=CuisineViewSet)
router.register(prefix='api/courses', viewset=CourseViewSet)
router.register(prefix='api/substitutions', viewset=SubstitutionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
    url(r'^api/pantry/', pantry_bindings, name='api-pantry'),
    url(r'^api/favorites/', favorites_bindings, name='api-favorites'),
    url(r'^api/search/$', search_recipes),
]
