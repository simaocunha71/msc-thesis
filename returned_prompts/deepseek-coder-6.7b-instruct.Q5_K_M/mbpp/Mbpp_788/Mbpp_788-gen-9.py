def new_tuple(list_val, string_val):
    return tuple(list_val) + (string_val,)

print(new_tuple(["WEB", "is"], "best"))  # ('WEB', 'is', 'best')


