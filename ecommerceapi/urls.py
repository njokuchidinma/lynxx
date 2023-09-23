"""
URL configuration for ecommerceapi project.

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
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
# from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


TITLE = 'Ecommerce API',
DESCRIPTION = 'A Web API for ecommerce websites.'
schema_view = get_schema_view(
    openapi.Info(
      title=TITLE,
      default_version='v1',
      description=DESCRIPTION,
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecommapi/v1/', include('api.urls')),
    # path('api/', include('router.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title=TITLE, description=DESCRIPTION)),
    path('redoc/', schema_view.with_ui('redoc'), name="swagger"),
    path('swagger/', schema_view.with_ui('swagger'), name="redoc"),
]
