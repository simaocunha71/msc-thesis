def tuple_intersection(*args):
    first_tuple = args[0]
    result = {first_tuple[i] for i in range(len(first_tuple))}
    for tuple_ in args[1:]:
        for elem in tuple_:
            if elem in result:
                result.add(elem)
    return result