from celery import shared_task
from datetime import datetime, timedelta
from AuthorBook import models as author_book_model


@shared_task
def makeArchive():
    current_date = datetime.now()
    ten_years_ago = current_date - timedelta(days=365*10)

    author_book_model.Book.objects.filter(publish_date__lte=ten_years_ago).update(is_archive=True)