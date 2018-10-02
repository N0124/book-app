from django.conf.urls import url

from books.views import BookListView, BookCreate, BookUpdate, BookDelete

urlpatterns = [
    url(r'^$', BookListView.as_view(), name='book-list'),
    url(r'^add/$', BookCreate.as_view(), name='book-add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', BookUpdate.as_view(), name='book-edit'),
    url(r'^delete/(?P<pk>[0-9]+)/$', BookDelete.as_view(), name='book-delete'),


]