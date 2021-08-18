from utils import get_json, write_file, make_code_string, get_args
from builder import Builder


if __name__ == '__main__':
    args = get_args()
    json_data = get_json(args.json)
    builder = Builder(json_data)
    dict_obj = builder.get_json_obj()
    write_file(make_code_string(dict_obj, args.name), args.output)
