def tuple_to_dict(tup):
    return {tup[i]: tup[i + 1] for i in range(0, len(tup), 2)}

# Test
print(tuple_to_dict((1, 5, 7, 10, 13, 5)))  # {1: 5, 7: 10, 13: 5}

