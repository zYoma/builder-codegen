import json

from dataclasses import make_dataclass
from distutils.util import strtobool
from typing import Union, Any

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

    def _rename_fields(self, data: dict) -> Union[dict, list]:
        """
        Метод позволяет рекурсивно переименовать поля в дикте с вложеными
        словарями/листами.

        :param data: на вход принимает словарь
        :return: рекурсия, либо дикт возвращается, либо список.
        """
        def _is_nested_type(obj):
            return type(obj) in [list, dict]

        if isinstance(data, list):
            return [
                self._rename_fields(obj) if _is_nested_type(obj) else obj
                for obj in data
            ]

        return {
            camel_case_to_snake_case(field_name): self._rename_fields(value)
            if _is_nested_type(value) else value
            for field_name, value in data.items()
        }

    def _get_nested_dataclass_dict(self, data: Union[dict, list]) -> Union[dict, list]:
        """
        Рекурсивный метод, позволяет из словаря с вложеной структурой создать
        дикт в котором каждая вложеная структура - отдельный датакласс.
        Приводит имена полей в snake_case.

        :param data: в первый раз на вход получает дикт, при последующих рекурсивных
                     вызовах может быть лист или дикт
        :return: в итоге вернет словарь. рекурсивные вызовы могут возвращать список.
        """
        def _is_nested_type(obj: Any) -> bool:
            return type(obj) in [list, dict]

        if isinstance(data, list):
            return [
                self._get_nested_dataclass_dict(obj)
                if _is_nested_type(obj) else obj
                for obj in data
            ]

        dataclass_dict = {}
        for field_name, value in data.items():
            # Если значение - это вложенный тип (лист или дикт), то идем в рекурсию
            if _is_nested_type(value):
                nested_value = self._get_nested_dataclass_dict(value)
                # Если в результате рекурсии вернулся дикт - создаем датакласс
                if isinstance(nested_value, dict):
                    value = make_dataclass(
                        field_name,
                        self._get_field_types(nested_value)
                    )(**nested_value)
                # Иначе нам прилетел список и нужно снова идти в рекурсию
                else:
                    value = self._get_nested_dataclass_dict(nested_value)

            dataclass_dict[camel_case_to_snake_case(field_name)] = value

        return dataclass_dict

    def get_dataclass_obj(self):
        """ Метод возвращет датакласс. """
        data = self._get_nested_dataclass_dict(self.json_data)
        fields = self._get_field_types(data)
        created_class = make_dataclass('JsonObject', fields)
        obj = created_class(**data)

        return obj

    def get_dict_obj(self):
        """ Метод возвращет словарь. """
        return self._rename_fields(self.json_data)
