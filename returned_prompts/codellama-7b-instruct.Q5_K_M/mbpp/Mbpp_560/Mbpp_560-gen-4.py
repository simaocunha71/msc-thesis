def union_elements(tuple1, tuple2):
    elements = tuple1 + tuple2
    return sorted(set(elements))

# OR

def union_elements(tuple1, tuple2):
    return sorted(set(tuple1 + tuple2))
