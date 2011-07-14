from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
     url(r"", include("holdingpage.subscriber.urls", namespace='subscriber', )),
     url(r'^admin/', include(admin.site.urls)),
)