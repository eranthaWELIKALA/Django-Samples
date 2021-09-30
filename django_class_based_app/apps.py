from django.apps import AppConfig


class DjangoClassBasedAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_class_based_app'
