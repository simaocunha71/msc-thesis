
def merge_dictionaries_three(dic1:dict,dic2:dict,dic3:dict)->dict:
  merged_dict = dic1.copy()
  merged_dict.update(dic2)
  merged_dict.update(dic3)
  return merged_dict


