def convert_list_dictionary(id_list, name_list, score_list):
    result = []
    for i in range(len(id_list)):
        id_dict = {id_list[i]: {name_list[i]: score_list[i]}}
        result.append(id_dict)
    return result