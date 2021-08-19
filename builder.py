import json

from dataclasses import make_dataclass, asdict
from distutils.util import strtobool
from typing import Union

from utils import camel_case_to_snake_case


class Builder:
    """
       Класс для автоматического создания датакласса из json.
       Конструктор принимает либо строку с сырым json, либо уже десериализованый словарь.
    """
    def __init__(self, data: Union[str, dict]):
        self.json_data = json.loads(data) if isinstance(data, str) else data

    @staticmethod
    def _get_field_types(data: dict):
        """
        Собирает список картежей ('имя_поля', 'тип поля')
        необходимый для создания датакласса.
        """
        cast_func_map = {
            bool: lambda value: bool(strtobool(value)),
            int: lambda value: int(value) if value else None,
            float: lambda value: float(value) if value else None,
            str: lambda value: str(value) if value else None,
            dict: lambda value: dict(value) if value else None,
            list: lambda value: list(value) if value else None,
        }

        return [
            (field_name, cast_func_map.get(type(value)))
            for field_name, value in data.items()
        ]

    def get_json_obj(self):
        data = {camel_case_to_snake_case(k): v for k, v in self.json_data.items()}
        fields = self._get_field_types(data)
        created_class = make_dataclass('JsonObject', fields)
        obj = created_class(**data)

        return asdict(obj)
