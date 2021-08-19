import argparse
import logging
import re
import sys
import json


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


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--json', help='JSON файл источник', default='data.json')
    parser.add_argument('-o', '--output', help='Имя выходного файла', default='result.py')
    parser.add_argument('-n', '--name', help='ИмяДатакласса:ИмяБилдера', required=True)
    return parser.parse_args()


def get_class_name(args_name: str):
    try:
        dataclass_name, builder_name = args_name.split(':')
    except ValueError:
        logging.error('Передайте в качестве параметра ИмяДаталасса:ИмяБилдера')
        sys.exit(1)

    return dataclass_name, builder_name


def get_json(filename: str = 'data.json') -> dict:
    with open(filename, "r") as f:
        data = json.load(f)

    return data


def write_file(data, filename: str = 'result.py'):
    with open(filename, "w") as f:
        for row in data:
            f.write(row)


def make_code_string(obj_data: dict, args_name: str) -> str:
    """
    Метод рисует выходной файл.
    Собираем список, где каждый элемент - отдельная строка.
    Возвращаем собранную строку серез \n

    :param obj_data: словарь с данными объекта
    :param args_name: строка с именами классов
    :return: собранная строка
    """
    dataclass_name, builder_name = get_class_name(args_name)

    def _make_class_rows(is_builder=False):
        self_ = '    self._' if is_builder else ''

        for field, value in obj_data.items():
            type_value = type(value)
            is_factory_types = type_value in [list, dict]
            string_type = TYPE_TO_STR.get(type_value, "str")
            default_value = ROW_TYPE[type_value] if is_factory_types else 'None'
            start_row = f'    {self_}{field}: '

            if is_factory_types and not is_builder:
                row = f'{start_row}{string_type} = field(default_factory=lambda: {default_value})'
            else:
                row = f'{start_row}Optional[{string_type}] = {default_value}'

            base_line.append(row)

    # dataclass
    base_line = ['@dataclass', f'class {dataclass_name}(BaseModel):']
    _make_class_rows()

    # builder
    base_line += [f'\n\nclass {builder_name}(BaseBuilder):', '    def __init__(self):', '        super().__init__()']
    _make_class_rows(is_builder=True)

    # методы билдера
    for field_name in obj_data.keys():
        base_line.append(f'\n    def with_{field_name}(self, {field_name}):')
        base_line.append(f'        self._{field_name} = {field_name}')
        base_line.append('        return self')

    # метод build
    base_line.append('\n    def build(self):')
    base_line.append(f'        return {dataclass_name}(')

    for field_name in obj_data.keys():
        base_line.append(f'            {field_name}=self._{field_name},')
    base_line.append('        ).asdict()')

    return '\n'.join(base_line)
