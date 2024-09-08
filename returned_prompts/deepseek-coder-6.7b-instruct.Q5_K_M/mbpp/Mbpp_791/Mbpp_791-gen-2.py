def remove_nested(tup):
    result = []
    for i in tup:
        if type(i) != tuple:
            result.append(i)
    return tuple(result)

print(remove_nested((1, 5, 7, (4, 6), 10)))

