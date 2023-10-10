from pydantic import BaseModel, validator


class EngineerName(BaseModel):
    name: str

    @validator("name")
    def validate_name_format(cls, value):

        # Подготовка фамилии и инициалов.
        parts = value.split()

        if len(parts) != 2:
            raise ValueError("Данные должны быть в формате: 'Фамилия И.О.'")

        last_name = parts[0]
        initials = parts[1].split('.')

        # Проверка формата Фамилии
        if not last_name.isalpha():
            raise ValueError("Фамилия должна состоять из букв")

        if not last_name[0].isupper():
            raise ValueError("Фамилия должна начинаться с заглавной буквы")

        if not last_name[1:].islower() and len(last_name) > 1:
            raise ValueError("Фамилия должна быть в нижнем регистре, кроме первой буквы")

        # Проверка формата инициалов.
        if len(initials) != 3:
            raise ValueError("Инициалы должны быть в формате 'И.О.'")

        if len(initials[0]) != 1 or len(initials[1]) != 1:
            raise ValueError("Каждый инициал должны состоять из одной буквы")

        if not (initials[0].isalpha() and initials[1].isalpha()):
            raise ValueError("Инициалы должны состоять из букв")


        if not (initials[0].isupper() and initials[1].isupper()):
            raise ValueError("Инициалы должны быть в верхнем регистре")

        return value
