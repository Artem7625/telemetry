import re
from pydantic import BaseModel, validator


class BaseNameValidator(BaseModel):
    """Класс валидации данных фамилии и инициалов."""

    name: str

    @validator("name")
    def validate_name_format(cls, value):
        # Регулярное выражение для формата "Фамилия И.О."
        pattern = r'^[А-ЯЁ][а-яё]+ [А-ЯЁ]\.[А-ЯЁ]\.$'

        if not re.match(pattern, value):
            raise ValueError("Данные должны быть в формате: 'Фамилия И.О.'")

        return value
