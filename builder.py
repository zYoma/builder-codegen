import json

from dataclasses import make_dataclass, asdict
from distutils.util import strtobool
from typing import Union


class Builder:
    """
       Класс для автоматического создания датакласса из json.
       Конструктор принимает либо строку с сырым json, либо уже десериализованый словарь.
    """
    def __init__(self, data: Union[str, dict]):
        self.json_data = json.loads(data) if isinstance(data, str) else data

    def _get_field_types(self):
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
            for field_name, value in self.json_data.items()
        ]

    def get_json_obj(self):
        fields = self._get_field_types()
        created_class = make_dataclass('JsonObject', fields)
        obj = created_class(**self.json_data)

        return asdict(obj)
