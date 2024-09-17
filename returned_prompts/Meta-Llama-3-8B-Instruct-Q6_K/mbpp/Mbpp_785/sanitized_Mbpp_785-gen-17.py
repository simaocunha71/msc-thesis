import ast
def tuple_str_int(s):
    try:
        return ast.literal_eval(s)
    except ValueError:
        return None  # or some other default value