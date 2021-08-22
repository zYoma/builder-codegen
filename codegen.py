from utils import (
    get_json,
    write_file,
    get_args, make_code_string,
    make_code_nested_dataclass
)
from builder import Builder


if __name__ == '__main__':
    args = get_args()
    json_data = get_json(args.json)
    builder = Builder(json_data)
    dict_obj = builder.get_dict_obj()
    nested_dataclass_code = make_code_nested_dataclass(
        obj_data=dict_obj,
        max_level=args.level,
    )
    write_file(data=nested_dataclass_code, filename=args.output)
    main_dataclass_code = make_code_string(
        obj_data=dict_obj,
        args_name=args.name,
    )
    write_file(data=main_dataclass_code, filename=args.output, append=True)
