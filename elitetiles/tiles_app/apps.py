from django.apps import AppConfig

class TilesAppConfig(AppConfig):
    name = 'tiles_app'

    def ready(self):
        import tiles_app.signals

