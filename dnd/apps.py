from django.apps import AppConfig
# from django.apps import AppConfig

class DndConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dnd'

    # default_auto_field = 'django.db.models.BigAutoField'
    # name = 'users'
    def ready(self):
        import dnd.signals  # noqa