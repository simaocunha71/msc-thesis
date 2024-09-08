def Extract(lst):
    return [sub[0] for sub in lst if isinstance(sub, list)]