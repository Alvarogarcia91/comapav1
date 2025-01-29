from django.core.exceptions import ValidationError
import re

class NumberValidator:
    def validate(self, password, user=None):
        if not re.search(r'\d', password):  # Verifica que la contraseña tenga al menos un número
            raise ValidationError("La contraseña debe contener al menos un número.")

    def get_help_text(self):
        return "Tu contraseña debe contener al menos un número."
