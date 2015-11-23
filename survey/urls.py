from django.conf.urls import include, url, patterns
from django.contrib import admin
print "+++++++++++"
urlpatterns = patterns('',
	url(r'^', include('apps.surveys.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
