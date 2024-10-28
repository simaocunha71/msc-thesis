def convert_list_dictionary(keys, names, values):
    return [{key: {name: value}} for key, name, value in zip(keys, names, values)]