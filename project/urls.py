from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('adminkareem219/', admin.site.urls),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('', include('realestate.urls')),
]



#handler404 = 'store.views.error_404_page'
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

