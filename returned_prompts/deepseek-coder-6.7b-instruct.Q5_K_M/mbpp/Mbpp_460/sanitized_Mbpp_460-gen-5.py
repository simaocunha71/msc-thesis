def Extract(lst):
    result = [i[0] for i in lst if isinstance(i, list)]
    return result