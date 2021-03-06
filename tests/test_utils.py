from utils import (
    make_code_string,  write_file, camel_case_to_snake_case, make_code_nested_dataclass
)

from .fixtures import *


def test_make_code_string(json_result, make_code_string_result):
    args_name = "TestFormData:TestFormDataBuilde"
    test_result = make_code_string(json_result, args_name)

    assert test_result == make_code_string_result


def test_get_class_name(json_result):
    args_name = ""
    with pytest.raises(SystemExit) as e:
        make_code_string(json_result, args_name)

    assert e.type == SystemExit
    assert e.value.code == 1


def test_camel_case_to_snake_case():
    test_case_1 = camel_case_to_snake_case('CamelCase')
    test_case_2 = camel_case_to_snake_case('case')
    test_case_3 = camel_case_to_snake_case('camel_case')

    assert test_case_1 == 'camel_case'
    assert test_case_2 == 'case'
    assert test_case_3 == 'camel_case'


def test_make_code_nested_dataclass(make_code_nested_dataclass_data, make_code_nested_dataclass_result):
    test_result = make_code_nested_dataclass(make_code_nested_dataclass_data, None)

    assert len(test_result) == make_code_nested_dataclass_result


def test_make_code_nested_dataclass_with_level(make_code_nested_dataclass_data):
    test_result = make_code_nested_dataclass(make_code_nested_dataclass_data, 1)

    assert len(test_result) == 10802


def test_make_code_nested_dataclass(make_code_nested_dataclass_data, make_code_nested_dataclass_result):
    test_result = make_code_nested_dataclass(make_code_nested_dataclass_data, None)

    assert len(test_result) == make_code_nested_dataclass_result
