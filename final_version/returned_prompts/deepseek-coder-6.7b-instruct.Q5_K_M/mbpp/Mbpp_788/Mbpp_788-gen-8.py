def new_tuple(lst, s):
    return tuple(lst) + (s,)

print(new_tuple(["WEB", "is"], "best"))  # -> ('WEB', 'is', 'best')

