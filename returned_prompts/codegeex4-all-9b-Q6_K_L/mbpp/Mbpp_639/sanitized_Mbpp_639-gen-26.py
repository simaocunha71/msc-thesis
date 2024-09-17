def sample_nam(namelist: list):
    new_namelist = [name for name in namelist if name[0].isupper()]
    return sum(len(name) for name in new_namelist)