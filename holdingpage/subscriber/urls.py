from django.conf.urls.defaults import *


urlpatterns = patterns("django.views.generic.simple",
                       url(r'^thank-you/$','direct_to_template', { 'template' : "subscriber/thank_you.html"}, name="thank_you"),
                       url(r'^successful-unsubscribe/$','direct_to_template', { 'template' : "subscriber/successful_unsubscribe.html"}, name="successful_unsubscribe"),)

urlpatterns += patterns("holdingpage.subscriber.admin_views",
                        url(r'^admin/data/export/$', 'export_csv', name="export_csv"),)

urlpatterns += patterns("holdingpage.subscriber.views",
                        url(r'^unsubscribe/(?P<email>.+)/$','unsubscribe_form', name="unsubscribe_form_with_email"),
                        url(r'^unsubscribe/$','unsubscribe_form', name="unsubscribe_form"),
                        url(r'^(?P<code>[0-9A-Z]{10})$','subscriber_form', name="subscriber_form_with_code"),
                        url(r'^$','subscriber_form', name="subscriber_form"),)