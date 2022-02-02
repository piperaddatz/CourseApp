from django.contrib.auth.base_user import BaseUserManager

import Appunte.models


# Cambios generales
# - Elimiados traductores

# confer: https://stackoverflow.com/questions/68601417/django-custom-user-model-migration-return-error-valueerror-related-model-use

# Cambios manager
# - Renombrado por claridad

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('rol', Appunte.models.ROL_STAFF)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('rol') == Appunte.models.ROL_STAFF:
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(email, password, **extra_fields)
