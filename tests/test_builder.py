from builder import Builder

from .fixtures import *


def test_build_with_str(string_data, string_data_result):
    builder = Builder(string_data)
    json_obj = builder.get_dict_obj()

    assert json_obj == string_data_result


def test_build_with_dict(dict_data, dict_data_result):
    builder = Builder(dict_data)
    json_obj = builder.get_dict_obj()

    assert json_obj == dict_data_result


def test_build_obj(json_data, json_result):
    builder = Builder(json_data)
    json_obj = builder.get_dict_obj()

    assert json_obj == json_result


def test_rename_fields(json_data, rename_fields_data, rename_fields_result):
    builder = Builder(json_data)
    test_data = builder._rename_fields(rename_fields_data)

    assert test_data == rename_fields_result


def test_get_nested_dataclass_dict(json_data, rename_fields_data, get_nested_dataclass_dict_result):
    builder = Builder(json_data)
    test_data = builder._get_nested_dataclass_dict(rename_fields_data)

    assert str(test_data) == get_nested_dataclass_dict_result
