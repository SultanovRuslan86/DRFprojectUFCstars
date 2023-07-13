"""
URL configuration for drfproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from UFCstars.views import UfcstarsAPIView, UfcstarAPIView, UfcstarAPIList, UfcstarAPIupdate, UfcCRUD, UfcstarsViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView

router = routers.DefaultRouter()
router.register(r'ufc', UfcstarsViewSet, basename='ufc')
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth', include('rest_framework.urls')),
    path('api/v1/ufcstarslist/', UfcstarsAPIView.as_view()),
    path('api/v1/Ufcstarlist/', UfcstarAPIView.as_view()),
    path('api/v1/UfcstarAPIlist/', UfcstarAPIList.as_view()),
    path('api/v1/Ufcstarlist/<int:pk>/', UfcstarAPIView.as_view()),
    path('api/v1/UfcstarUpdate/<int:pk>/', UfcstarAPIupdate.as_view()),
    path('api/v1/UfcstarCRUD/<int:pk>/', UfcCRUD.as_view()),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]












