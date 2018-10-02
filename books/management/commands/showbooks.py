from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    help = 'Display	list of	books'

    def add_arguments(self, parser):
        parser.add_argument('-o', '--order', type=str, help='Define asc/desc ordering by publish date')

    def handle(self, *args, **options):

        books = Book.objects.all()
        order = options.get('order')

        if order == 'asc':
            books = books.order_by('publish_date')
        elif order == 'desc':
            books = books.order_by('-publish_date')

        self.stdout.write(self.style.SUCCESS('\n'.join([f'{book.title} by {book.author}'for book in books])))
