from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "oasis.users"
    verbose_name = "Users"

    def ready(self):
        from .signals import user_signed_up
