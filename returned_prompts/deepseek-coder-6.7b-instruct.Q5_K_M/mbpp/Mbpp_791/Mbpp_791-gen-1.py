
def remove_nested(tup):
    return tuple(i for i in tup if not isinstance(i, tuple))

print(remove_nested((1, 5, 7, (4, 6), 10)))


