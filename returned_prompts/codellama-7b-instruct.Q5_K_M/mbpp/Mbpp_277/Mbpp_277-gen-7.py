
def dict_filter(my_dict: dict,n: int) -> dict:
  return {key:value for key,value in my_dict.items() if value>=n}


