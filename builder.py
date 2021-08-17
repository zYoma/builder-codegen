from typing import Union
import json

from dataclasses import make_dataclass
from distutils.util import strtobool


def get_json(filename: str = 'data.json') -> dict:
    with open(filename, "r") as f:
        data = json.load(f)

    return data


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
        }

        return [
            (field_name, cast_func_map.get(type(value)))
            for field_name, value in self.json_data.items()
        ]

    def get_json_obj(self):
        fields = self._get_field_types()
        created_class = make_dataclass('JsonObject', fields)
        obj = created_class(**self.json_data)

        return obj


if __name__ == '__main__':
    json_data = get_json()  # Как-то полученный JSON
    builder = Builder(json_data)
    json_obj = builder.get_json_obj()
    print(json_obj.__dict__)
