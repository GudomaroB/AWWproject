from django.core.exceptions import ValidationError


def validate_not_empty(value):
    # Проверка "а заполнено ли поле?"
    if value == "":
        raise ValidationError(
            "Пустое поле",
            params={"value": value},
        )
