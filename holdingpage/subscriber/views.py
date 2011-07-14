from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from holdingpage.subscriber.forms import SubscriberForm
from holdingpage.subscriber.models import Subscriber


def subscriber_form(request, code=None):
    """
    The default view for the app, simply provides a subscriber form
    that saves a name and email address to the subscriber database
    """
    initial = {}
    if code is not None:
        referrer = get_object_or_404(Subscriber, share_code=code)
        initial['source_share_code'] = code

    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            return HttpResponseRedirect(reverse('subscriber:thank_you'))
    else:
        form = SubscriberForm(initial=initial)
    context = { 'form' : form }
    return render_to_response("subscriber/subscriber_form.html", 
                              context,
                              RequestContext(request))