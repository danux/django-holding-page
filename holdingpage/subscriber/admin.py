from django.contrib.admin import site
from holdingpage.subscriber.models import Subscriber


site.register(Subscriber)