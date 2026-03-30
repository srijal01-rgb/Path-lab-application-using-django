from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import PatientViewSet, TestViewSet, LabReportViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'tests', TestViewSet)
router.register(r'labreports', LabReportViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="LabTech API",
      default_version='v1',
      description="API documentation for LabTech Path Lab",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
