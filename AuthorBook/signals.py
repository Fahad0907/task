from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from AuthorBook import models as author_book_model


@receiver(post_save, sender=author_book_model.Book)
def log_create_update(sender, instance , created, **kwargs):
    action_type = 'Create' if created else 'Update'

    author_book_model.LogTable.objects.create(
        book_name=instance.title,
        action = action_type,
    )
    
@receiver(post_delete, sender=author_book_model.Book)

def log_delete(sender, instance, **kwargs):
    author_book_model.LogTable.objects.create(
        book_name=instance.title,
        action = "Delete",
    )