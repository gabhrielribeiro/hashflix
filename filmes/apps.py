from django.apps import AppConfig


class FilmesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filmes'

    def ready(self):
        from contas.models import Usuario
        import os

        email = os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")

        if not email or not senha:
            return

        if not Usuario.objects.filter(username="admin").exists():
            Usuario.objects.create_superuser(
                username="admin",
                email=email,
                password=senha,
                is_active=True,
                is_staff=True
            )