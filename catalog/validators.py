from django.core.exceptions import ValidationError

from .constants import FORBIDDEN_WORDS


def validate_no_forbidden_words(value: str) -> None:
    """Проверяет, что в тексте нет запрещённых слов (регистр игнорируется)."""
    value_lower = value.lower()
    for word in FORBIDDEN_WORDS:
        if word.lower() in value_lower:
            raise ValidationError(
                f'Слово "{word}" запрещено использовать в названии и описании продукта.'
            )
