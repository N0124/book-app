import logging

from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from books.forms import EditBookForm, CreateBookForm
from books.models import Book

logger = logging.getLogger(__name__)


class BookListView(ListView):

    model = Book


@method_decorator(staff_member_required, name='dispatch')
class BookUpdate(UpdateView):

    model = Book
    form_class = EditBookForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('book-list')

    def post(self, request, *args, **kwargs):
        response = super(BookUpdate, self).post(request, *args, **kwargs)
        logger.info(f'Edit book id #{kwargs["pk"]}')
        return response


@method_decorator(staff_member_required, name='dispatch')
class BookCreate(CreateView):
    model = Book
    form_class = CreateBookForm
    success_url = reverse_lazy('book-list')

    def post(self, request, *args, **kwargs):
        response = super(BookCreate, self).post(request, *args, **kwargs)
        logger.info(f'Create book {request.POST["title"]}')
        return response


@method_decorator(staff_member_required, name='dispatch')
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')

    def post(self, request, *args, **kwargs):
        response = super(BookDelete, self).post(request, *args, **kwargs)
        logger.info(f'Delete book id #{kwargs["pk"]}')
        return response
