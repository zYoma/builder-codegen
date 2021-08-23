import argparse
import logging
import re
import sys
import json

from typing import Union


GLOBAL_DICT = {}

TYPE_TO_STR = {
    bool: 'bool',
    int: 'int',
    float: 'float',
    str: 'str',
    dict: 'dict',
    list: 'list',
}


ROW_TYPE = {
    list: [],
    dict: {},
}


def camel_case_to_snake_case(name: str) -> str:
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    snake_name = pattern.sub('_', name).lower()

    return snake_name


def to_camel_case(snake_str: str) -> str:
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--json', help='JSON файл источник', default='data.json')
    parser.add_argument('-o', '--output', help='Имя выходного файла', default='result.py')
    parser.add_argument('-n', '--name', help='ИмяДатакласса:ИмяБилдера', required=True)
    parser.add_argument('-l', '--level', help='Максимальный уровень вложенности', default=None , type=int)
    return parser.parse_args()


def get_class_name(args_name: str):
    try:
        dataclass_name, builder_name = args_name.split(':')
    except ValueError:
        logging.error('Передайте в качестве параметра ИмяДаталасса:ИмяБилдера')
        sys.exit(1)

    return dataclass_name, builder_name


def get_json(filename: str = 'data.json') -> dict:
    with open(filename, "r", encoding="utf8") as f:
        data = json.load(f)

    return data


def write_file(data, filename: str = 'result.py', append=False):
    write_type = "a" if append else "w"
    with open(filename, write_type) as f:
        for row in data:
            f.write(row)


def make_global_dict(
        data: Union[dict, list],
        max_level: Union[int, None],
        level: int = 0,
        parent: str = '',
) -> None:
    """
    Рекурсивно обходим словарь. Формируем GLOBAL_DICT, где ключи - это путь(строка) до
    вложенного объекта через разделитель __, значения - значения вложенного объекта.

    :param data: при первом вызове - исходный словарь, при рекурсивных вызовах -
                вложенный список или дикт
    :param max_level: максимальный уровень вложенности
    :param level: текущий уровень
    :param parent: строка с путем до родительского объекта
    """
    if max_level is not None and level > max_level:
        return

    next_level = level + 1

    if isinstance(data, list):
        [
            make_global_dict(
                data=obj,
                level=next_level,
                parent=f'{parent}__{num}',
                max_level=max_level,
            )
            for num, obj in enumerate(data)
        ]

    if isinstance(data, dict):
        for field_name, value in data.items():
            if isinstance(value, dict):
                next_parent = f'{parent}__{field_name}'
                GLOBAL_DICT[next_parent] = value

                make_global_dict(
                    data=value,
                    level=next_level,
                    parent=next_parent,
                    max_level=max_level
                )
            if isinstance(value, list):
                next_parent = f'{field_name}'

                make_global_dict(
                    data=value,
                    level=next_level,
                    parent=next_parent,
                    max_level=max_level
                )


def make_code_nested_dataclass(obj_data: dict, max_level: int) -> str:
    """
    Функция для генерации кода всех вложенных датаклассов.
    :param obj_data: исходный словарь
    :param max_level: саксимальный уровень вложенности
    :return: сгенерированный код
    """
    make_global_dict(obj_data, max_level)
    code = ''

    # Сортируем по уровню вложенности для того, чтобы в генерируемом файле сперва
    # шли датаклассы с максимальной вложенностью
    sorted_dict = dict(sorted(
        GLOBAL_DICT.items(),
        key=lambda x: len(x[0].split('__')),
        reverse=True)
    )

    for path in sorted_dict:
        if obj_data := sorted_dict[path]:
            code += make_code_string(
                obj_data=obj_data,
                args_name=f'{path}:{path}_builder',
                nested=True,
            )
            code += '\n\n'

    return code


def make_code_string(obj_data: dict, args_name: str, nested: bool = False) -> str:
    """
    Метод рисует выходной файл.
    Собираем список, где каждый элемент - отдельная строка.
    Возвращаем собранную строку серез \n

    :param obj_data: словарь с данными объекта
    :param args_name: строка с именами классов
    :param nested: для вложенных датаклассов или для основного
    :return: собранная строка
    """
    dataclass_name, builder_name = get_class_name(args_name)
    camel_case_dataclass_name = to_camel_case(dataclass_name)
    camel_case_builder_name = to_camel_case(builder_name)
    if not nested:
        camel_case_builder_name = builder_name
        camel_case_dataclass_name = dataclass_name

    def _make_class_rows(is_builder=False):
        self_ = '    self._' if is_builder else ''

        for field, value in obj_data.items():
            type_value = type(value)
            is_factory_types = type_value in [list, dict]
            string_type = TYPE_TO_STR.get(type_value, "str")
            default_value = ROW_TYPE[type_value] if is_factory_types else 'None'
            start_row = f'    {self_}{field}: '
            camel_case_field = to_camel_case(field)
            dataclass_field_default_value = f'Optional[{string_type}] = {default_value}' \
                if is_builder else f'{string_type} = field(default_factory=lambda: {default_value})'

            original_class_name = f'{dataclass_name}__{field}' if nested else f'__{field}'
            class_name = f'{camel_case_dataclass_name}{camel_case_field}' if nested else f'{camel_case_field}'
            dataclass_field_value = f'Optional[{class_name}] = None' if GLOBAL_DICT.get(
                f'{original_class_name}') else dataclass_field_default_value

            if is_factory_types:
                row = f'{start_row}{dataclass_field_value}'
            else:
                row = f'{start_row}Optional[{string_type}] = {default_value}'

            base_line.append(row)

    # dataclass
    base_line = ['@dataclass', f'class {camel_case_dataclass_name}(BaseModel):']
    _make_class_rows()

    # builder
    base_line += [f'\n\nclass {camel_case_builder_name}(BaseBuilder):', '    def __init__(self):', '        super().__init__()']
    _make_class_rows(is_builder=True)

    # методы билдера
    for field_name in obj_data.keys():
        base_line.append(f'\n    def with_{field_name}(self, {field_name}):')
        base_line.append(f'        self._{field_name} = {field_name}')
        base_line.append('        return self')

    # метод build
    base_line.append('\n    def build(self):')
    base_line.append(f'        return {camel_case_dataclass_name}(')

    for field_name in obj_data.keys():
        base_line.append(f'            {field_name}=self._{field_name},')
    base_line.append('        ).asdict()')

    return '\n'.join(base_line)
