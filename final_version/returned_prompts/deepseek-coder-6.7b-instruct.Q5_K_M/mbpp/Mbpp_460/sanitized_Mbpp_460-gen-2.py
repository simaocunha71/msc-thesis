def Extract(lst):
    return [sublist[0] for sublist in lst if isinstance(sublist, list)]