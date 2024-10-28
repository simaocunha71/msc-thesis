def drop_empty(dict_):
    for k, v in dict_.items():
        if v is None:
            del dict_[k]
    return dict_