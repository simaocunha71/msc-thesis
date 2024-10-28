def concatenate_tuple(tup):
    return '-'.join(map(str, tup)) if all(isinstance(i, (int, str)) for i in tup) else 'Invalid input'  #map(str, tup) converts each element to string before joining