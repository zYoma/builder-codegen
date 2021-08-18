from utils import make_code_string,  write_file

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
