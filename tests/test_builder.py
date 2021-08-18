from builder import Builder

from .fixtures import *


def test_build_with_str(string_data, string_data_result):
    builder = Builder(string_data)
    json_obj = builder.get_json_obj()

    assert json_obj == string_data_result


def test_build_with_dict(dict_data, dict_data_result):
    builder = Builder(dict_data)
    json_obj = builder.get_json_obj()

    assert json_obj == dict_data_result


def test_build_obj(json_data, json_result):
    builder = Builder(json_data)
    json_obj = builder.get_json_obj()

    assert json_obj == json_result
