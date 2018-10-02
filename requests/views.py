from django.views.generic import ListView

from requests.models import Request


class RequestListView(ListView):

    model = Request
    queryset = Request.objects.order_by('-time')[:10]
