from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('pre_recording/', include('pre_recording.urls')),
                  path('', include('landing_page.urls'))

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
