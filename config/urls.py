from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve 
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/accounts/login')),
    path('accounts/', include('accounts.urls')),
    path('shopTip/', include('shopTip.urls')),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)