from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ingredient import views


router = DefaultRouter()
router.register('ingredient', views.IngredientViewSet)

app_name = 'ingredient'

urlpatterns = [
    path('', include(router.urls))
]