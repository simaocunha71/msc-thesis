def convert_list_dictionary(keys, values1, values2):
    output = []
    for i in range(len(keys)):
        temp_dict = {keys[i]: {values1[i]: values2[i]}}
        output.append(temp_dict)
    return output
keys = ["S001", "S002", "S003", "S004"]
values1 = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]
values2 = [85, 98, 89, 92]