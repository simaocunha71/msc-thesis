def extract_string(lst,size):
    return [i for i in lst if type(i) == str and len(i) > size]