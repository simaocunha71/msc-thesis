
def convert_list_dictionary(keys: list,values1: list,values2: list) -> list:
  return [{keys[i]: {values1[i]: values2[i]}} for i in range(len(keys))]


