from pydantic import BaseModel, validator

from . validators import BaseNameValidator


class EngineerName(BaseNameValidator, BaseModel):
    """Класс, описывающий модель фамилии и инициалов пользователя."""

    name: str

    @validator("name")
    def validate_name(cls, value):
        return cls.validate_name_format(value)
