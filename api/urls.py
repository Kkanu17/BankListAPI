from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('bank', views.BankViewSet)
router.register('branches', views.BranchesViewSet)

# SessionAuthentication is implemented 

urlpatterns = [
   
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]