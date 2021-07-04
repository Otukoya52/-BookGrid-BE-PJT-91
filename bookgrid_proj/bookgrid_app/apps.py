from django.apps import AppConfig


class BookgridAppConfig(AppConfig):
    name = 'bookgrid_app'

    def ready(self):
        import bookgrid_app.signals
