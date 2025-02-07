from django.apps import AppConfig


class CbvCrudAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cbv_crud_app'

    
    def ready(self):
        import cbv_crud_app.signals