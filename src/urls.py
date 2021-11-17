from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('pages.urls')),
	path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
	#url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    #url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
