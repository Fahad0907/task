from django.apps import AppConfig


class AuthorbookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AuthorBook'

    def ready(self) -> None:
        import AuthorBook.signals
