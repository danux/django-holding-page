from django.contrib import admin
from holdingpage.subscriber.models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subscribers_recruited')
admin.site.register(Subscriber, SubscriberAdmin)