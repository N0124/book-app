from django.conf.urls import url

from requests.views import RequestListView

urlpatterns = [
    url(r'^$', RequestListView.as_view(), name='request-list')]