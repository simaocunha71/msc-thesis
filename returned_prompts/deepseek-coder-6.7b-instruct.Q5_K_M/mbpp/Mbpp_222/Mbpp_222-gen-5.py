
def check_type(tup):
    return all(isinstance(element, type(tup[0])) for element in tup[1:])


